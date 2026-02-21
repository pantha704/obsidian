# Telemetry & Event System (Issue #5) Explanation

This document breaks down exactly what the `src/telemetry.rs` file does in the Scheduler project, line by line, in plain English.

**Telemetry** is just a fancy word for "collecting data from a distant place." In our case, the "distant place" is the Scheduler running in the background, and the "data" is the system's memory, CPU, and event logs.

## Part 1: Setting up the Event Logger (`init_telemetry`)

This function builds the pipeline that captures messages (like "Job started" or "Job failed") and saves them so we can read them later.

```rust
pub fn init_telemetry() -> tracing_appender::non_blocking::WorkerGuard {
```

**What it means:** We are defining a function called `init_telemetry`. It returns a "guard" object. As long as this guard exists, the background thread writing our logs to the file is kept alive.

```rust
    // 1. File Logger (rolling daily)
    let file_appender = tracing_appender::rolling::daily("logs", "scheduler.log");
```

**What it means:** This creates a tool that knows how to write to files. Specifically, it will create a new file every day inside a folder called `logs`, and name the file `scheduler.log.YYYY-MM-DD`. This is called "rolling daily"—it prevents one giant log file from filling up your entire hard drive over a year.

```rust
    let (non_blocking, guard) = tracing_appender::non_blocking(file_appender);
```

**What it means:** Writing to a hard drive is slow. If the scheduler had to wait for the hard drive every time it logged a message, it would ruin the performance. This line wraps our file writer in a "non_blocking" layer. It creates a completely separate background thread that handles the slow file-writing, so our main program never slows down.

```rust
    // Create layer for file output
    let file_layer = tracing_subscriber::fmt::layer()
        .with_writer(non_blocking)
        .with_ansi(false);
```

**What it means:** This creates the "formatting" for the file output. We tell it to use the `non_blocking` writer we just made, and we turn off `ANSI` colors (because text files look weird if they are full of invisible terminal color codes).

```rust
    // 2. Terminal Logger
    let stdout_layer = tracing_subscriber::fmt::layer()
        .with_writer(std::io::stdout);
```

**What it means:** This creates a second formatting layer, but this one is meant to print directly to your terminal screen (`std::io::stdout`). This one _does_ keep colors enabled by default so it looks pretty when you read it live.

```rust
    // Combine both layers
    let subscriber = tracing_subscriber::registry()
        .with(LevelFilter::INFO)
        .with(stdout_layer)
        .with(file_layer);
```

**What it means:** This bundles everything together into one master "subscriber". We attach both the terminal output (`stdout_layer`) and the file output (`file_layer`). We also add a `LevelFilter::INFO`, which means "only record messages that are INFO, WARNING, or ERROR. Ignore extreme underlying DEBUG or TRACE noise."

```rust
    // Set as global
    let _ = tracing::subscriber::set_global_default(subscriber);
    info!("Event System & Telemetry initialized.");
```

**What it means:** We inject this master subscriber globally into the application. Now, anywhere else in the code (like inside our `Job` struct), if someone types `info!("Hello")`, it will automatically format it and send it to both the terminal and the daily text file! We immediately test it by logging "Event System & Telemetry initialized."

```rust
    guard
}
```

**What it means:** We return the `guard` so the main program can hold onto it. If we didn't do this, the background worker thread we created earlier would instantly die, and nothing would get written to the file!

---

## Part 2: Tracking Machine Resources (`log_resource_usage`)

This function specifically looks at the physical computer running the scheduler to see how hard it's working.

```rust
pub fn log_resource_usage() {
    let mut sys = System::new_all();
```

**What it means:** We create a new `sysinfo` object that acts as a probe into your computer’s operating system.

```rust
    sys.refresh_all();
    std::thread::sleep(sysinfo::MINIMUM_CPU_UPDATE_INTERVAL);
    sys.refresh_all();
```

**What it means:** Calculating CPU usage is tricky—you can't just take an instant snapshot; you have to measure it over a tiny slice of time. We take snapshot #1, sleep for a fraction of a second (the minimum required), and then take snapshot #2. The difference between those two snapshots tells us the exact CPU percentage being used!

```rust
    let total_memory = sys.total_memory() / 1024 / 1024; // MB
    let used_memory = sys.used_memory() / 1024 / 1024; // MB
```

**What it means:** We ask the system for its total RAM and how much RAM is currently being used. By default, it tells us this in "Bytes". That's a huge, unreadable number. We divide it by 1024 to get Kilobytes, and divide by 1024 again to get Megabytes (MB).

```rust
    let cpu_usage = sys.global_cpu_usage();
```

**What it means:** We grab the total global CPU percentage calculated between our two snapshots above.

```rust
    info!(
        "Resource Monitor - Memory: {}MB / {}MB, CPU: {:.2}%",
        used_memory, total_memory, cpu_usage
    );
}
```

**What it means:** Finally, we use our global logging system (built in Part 1) to emit an `INFO` event containing the memory and CPU. The `{:.2}%` ensures the CPU percentage is rounded to a nice, clean two decimal places, preventing a giant ugly string of numbers.
