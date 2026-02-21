# Turbin3 Scheduler Overall Architecture

This document maps out how all 6 of the active issues in the `scheduler` project connect to form the final production application.

## System Diagram (ASCII)

```text
                                +-------------------+
                                |    Issue #4       |
          [Add/Remove Jobs] --> | CLI Interface     | --> [Displays logs to User]
                                +---------+---------+
                                          |
                                          v
+---------------------------------------------------------------------------------+
|                                CORE ENGINE                                      |
|                                                                                 |
|   +-------------------+                           +-------------------------+   |
|   |    Issue #1       | <--(Pop next ready)------ |       Issue #2          |   |
|   | Queue Manager     |                           | Time & Priority Engine  |   |
|   | (Holds Pending)   | ------(Poll current_time & execution_time)--------> |   |
|   +---------+---------+                           +-----------+-------------+   |
|             |                                                 |                 |
|             v                                                 |                 |
|   +-------------------+                                       |                 |
|   |    Issue #6       |           (Yes, Current Time >= Execution Time)         |
|   | Storage System    |                                       |                 |
|   | (queue.json)      |                                       |                 |
|   +-------------------+                                       v                 |
|                                                     +-----------------------+   |
|                                                     |      Issue #3         |   |
|         ^                                           | Worker Executor       |   |
|         |                                           +-----------+-----------+   |
|         |                                                       |               |
+---------|-------------------------------------------------------|---------------+
          |                                                       |
          |               +---------------------------------------+
          |               | (Executes job.start())
          |               v
          |     +-------------------+
          |     |    Job Payload    |
          |     | (Actual Function) |
          |     +---------+---------+
          |               |
          |               v
    [retry_count < max?]  |
  +------(If True)--------+-------+
  |                               |
  |     +-------------------+     |
  +---- |job.fail_and_retry()|    |     +-------------------+
        +---------+---------+     +---> | job.complete()    |
                  |                     +---------+---------+
                  |                               |
                  |                               |
+-----------------v-------------------------------v-------------------------------+
|      Issue #5: Event System & Telemetry (Listens to ALL state changes)          |
|                                                                                 |
|                   Emit INFO/WARN Logs & CPU/Memory Stats                        |
|                                                                                 |
|   +-------------------------+                 +-----------------------------+   |
|   | Terminal / CLI display  |                 | logs/scheduler.log disk file|   |
|   +-------------------------+                 +-----------------------------+   |
+---------------------------------------------------------------------------------+
```

## Component Breakdowns

**Issue #1: Queue Manager**
The central hub. It's a memory array (likely a Min-Heap or Binary Tree) that stores all `Pending` jobs.

**Issue #2: Time & Priority Engine**
The "Clock". In production, this system constantly polls the Queue Manager. It glances at the very first job in line (`peek()`). If the current real-world time has passed the job's `execution_time`, it `pop()`s it out of the queue and hands it to the Worker. If two times are identical, it uses `priority` to tiebreak.

**Issue #3: Worker Executor**
The "Muscle". It takes the job handed to it by the Engine. It tells our code `job.start()`, and then actually attempts to run the `Job`'s internal function pointer payload. If it finishes cleanly, it calls `job.complete()`. If it panics/fails, it routes to `job.fail_and_retry()`. If that retry returns `true`, the Worker Executor throws it back into the Queue Manager to try again.

**Issue #4: CLI (Command Line Interface)**
The "Dashboard". Likely using a library like `ratatui`, this gives the user a visual terminal display where they can watch jobs cycle through, add new jobs, or delete existing ones.

**Issue #5: Event System & Telemetry** _(Our Code!)_
The "Nervous System". Operates globally across the entire app. It listens for any state transition methods (the `start()`, `complete()`, `fail()` functions) being triggered by the Worker Executor. It immediately routes those updates to the CLI's terminal stream and records them permanently to `scheduler.log`.

**Issue #6: Scheduler Memory** _(Our Code!)_
The "Save State". Since the Queue Manager only stores jobs in active RAM, power loss means lost jobs. The Queue Manager will route its data through our `serde` Storage module every time an item is pushed/popped, instantly overwriting `queue.json` on disk to ensure physical disaster recovery.
