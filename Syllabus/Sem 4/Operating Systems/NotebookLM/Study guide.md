
Operating System Concepts and Algorithms Study Guide

**Quiz**

1. What is the primary function of an operating system?
2. Briefly explain the purpose of a bootstrap program during system startup.
3. How does a system call act as an interface between user programs and the operating system kernel?
4. Define the term "interrupt" in the context of operating systems.
5. What is the main difference between a single-process system and a multi-process system?
6. Describe the concept of "time-slicing" as used in time-sharing operating systems.
7. What are the key roles of the kernel and the shell in an operating system?
8. Explain why a thread is sometimes called a "lightweight process."
9. In process scheduling, what distinguishes preemptive scheduling from non-preemptive scheduling?
10. What is internal fragmentation and what causes it?

**Quiz Answer Key**

1. An operating system manages computer hardware and software resources, providing common services for computer programs and acting as an intermediary between the user and hardware for efficient and secure operation.
2. The bootstrap program is the first code executed when a computer starts. It is stored in non-volatile memory and is responsible for initializing the system and loading the operating system into RAM.
3. A system call allows a program to request services from the operating system kernel, enabling interaction with underlying system resources like hardware, memory, and files.
4. An interrupt is a signal from hardware or software that alerts the processor to a high-priority process or event requiring immediate attention, interrupting the current process.
5. A single-process system can execute only one process at a time, while a multi-process system can execute multiple processes concurrently or simultaneously, leading to better CPU utilization.
6. Time-slicing is the technique used in time-sharing systems where the CPU switches rapidly between users, giving each user a small time slice of CPU time to create the illusion of simultaneous access.
7. The kernel is the core of the OS, managing hardware and resources, while the shell is an interface (often command-line) that interprets user commands and passes them to the kernel for execution.
8. A thread is called a lightweight process because it is the smallest unit of CPU execution within a process and shares the same memory space and resources as other threads within that process, using less overhead.
9. Preemptive scheduling allows the OS to interrupt a running process and move it back to the ready queue, while non-preemptive scheduling allows a process to run to completion or until it voluntarily gives up the CPU.
10. Internal fragmentation is wasted space inside an allocated memory block, caused by fixed-size memory allocation where a process is given slightly more memory than it actually needs.

**Essay Questions**

1. Compare and contrast the First-Come, First-Served (FCFS), Shortest Job First (SJF), and Shortest Remaining Time First (SRTF) process scheduling algorithms, discussing their advantages, disadvantages, and typical use cases.
2. Explain the concept of virtual memory and discuss how paging, page tables, and demand paging work together to implement it. Include a discussion of the role of the Translation Lookaside Buffer (TLB).
3. Describe the problem of deadlock in operating systems, outlining the four necessary conditions for deadlock to occur. Discuss common strategies for deadlock prevention, avoidance, and detection.
4. Analyze the Bounded Buffer Problem and the Readers and Writers Problem as classic synchronization challenges. Explain how semaphores can be used to provide solutions to these problems, detailing the roles of different semaphore types.
5. Compare and contrast the FCFS, SSTF, SCAN, and C-SCAN disk scheduling algorithms. For each algorithm, describe its approach, discuss its pros and cons in terms of performance metrics like total head movement and fairness, and consider scenarios where each might be most suitable.

**Glossary of Key Terms**

- **Operating System (OS):** System software that manages computer hardware and software resources and provides services for programs.
- **Bootstrap Program:** The initial code executed on system startup, responsible for initializing hardware and loading the OS.
- **System Call:** A mechanism for a program to request a service from the operating system kernel.
- **Interrupt:** A signal (hardware or software) alerting the processor to an event needing immediate attention.
- **Main Memory (RAM):** Primary storage directly accessible by the CPU; fast but volatile.
- **Secondary Storage:** Non-volatile storage with large capacity (e.g., HDDs, SSDs).
- **File System:** A method for organizing data on secondary storage using directories and files.
- **Swap Space:** Area on secondary storage used for virtual memory, storing pages swapped out of RAM.
- **Cache Memory:** High-speed memory between the CPU and RAM storing frequently accessed data.
- **Virtual Memory:** An abstraction providing processes the illusion of large, contiguous memory, using disk space to extend RAM.
- **Logical Address (Virtual Address):** The address generated by the CPU, seen by the program.
- **Physical Address:** The actual location in main memory.
- **Swapping:** Moving processes temporarily between main memory and secondary storage.
- **Fragmentation:** Inefficient memory usage leaving unusable gaps or pieces of free space.
- **Internal Fragmentation:** Wasted space _inside_ allocated memory blocks due to fixed-size allocation.
- **External Fragmentation:** Wasted space _outside_ allocated blocks, where free memory is scattered in small, non-contiguous pieces.
- **Paging:** Memory management technique dividing memory into fixed-size pages and frames to eliminate external fragmentation.
- **Page:** A fixed-size block of logical memory.
- **Frame:** A fixed-size block of physical memory.
- **Page Table:** Data structure mapping logical pages to physical frames.
- **Segmentation:** Memory management technique dividing memory into variable-sized segments based on logical divisions.
- **Segment Table:** Data structure storing base address and limit (size) for each segment.
- **Demand Paging:** A virtual memory technique where pages are loaded into memory only when they are needed (referenced) during execution.
- **Page Fault:** Occurs when a process attempts to access a page not currently in memory.
- **Page Replacement Algorithm:** Used to decide which page to swap out of memory when a page fault occurs and memory is full.
- **FIFO (First-In First-Out) Page Replacement:** Replaces the oldest page in memory.
- **LRU (Least Recently Used) Page Replacement:** Replaces the page that has not been used for the longest time.
- **Optimal Page Replacement:** Replaces the page that will not be used for the longest time in the future (theoretically optimal, but not practical).
- **Belady's Anomaly:** The phenomenon where increasing the number of page frames can sometimes increase the number of page faults (observed in FIFO).
- **Thrashing:** Excessive page swapping between RAM and disk, causing the system to slow down significantly.
- **Working Set:** The set of pages actively used by a process at a given time.
- **Translation Lookaside Buffer (TLB):** A small, fast cache storing recent page table entries to speed up address translation.
- **TLB Hit:** The virtual address is found in the TLB.
- **TLB Miss:** The virtual address is not found in the TLB, requiring a page table lookup.
- **Effective Memory Access Time (EMAT):** The average time taken to access memory, considering both TLB access time and memory access time, influenced by the TLB hit ratio.
- **Process:** An instance of a program in execution; a dynamic entity with states.
- **Process Control Block (PCB):** A data structure containing information about a process (state, PC, registers, memory info, etc.).
- **Context Switching:** The process of saving the state of one process and loading the state of another to switch CPU execution.
- **Thread:** The smallest unit of CPU execution within a process; shares process resources but has its own PC, registers, and stack.
- **User-Level Threads:** Threads managed by a user-level library, faster but not known to the OS.
- **Kernel-Level Threads:** Threads managed directly by the OS kernel, allowing true parallelism but with more overhead.
- **Hybrid Threads:** Combines user-level and kernel-level threads.
- **Process Scheduling:** The task of deciding which process gets CPU time and for how long.
- **Scheduler:** The OS component responsible for selecting processes for CPU execution.
- **Long-Term Scheduler (Job Scheduler):** Controls the admission of processes into the system (degree of multiprogramming).
- **Short-Term Scheduler (CPU Scheduler):** Selects the next process to execute from the ready queue.
- **Dispatcher:** The module that gives control of the CPU to the process selected by the short-term scheduler.
- **Dispatch Latency:** The time taken by the dispatcher to stop one process and start another.
- **CPU Utilization:** The percentage of time the CPU is busy executing processes.
- **Throughput:** The number of processes completed per unit time.
- **Turnaround Time:** The total time from process submission to completion.
- **Waiting Time:** The time a process spends waiting in the ready queue.
- **Response Time:** The time from request submission until the first response is produced.
- **Preemptive Scheduling:** CPU can be taken away from a running process.
- **Non-Preemptive Scheduling:** Process runs until it finishes or waits.
- **FCFS (First-Come, First-Served):** Processes executed in arrival order.
- **SJF (Shortest Job First):** Selects the process with the shortest burst time (non-preemptive).
- **SRTF (Shortest Remaining Time First):** Preemptive version of SJF, selects the process with the shortest remaining burst time.
- **Round Robin (RR):** Each process gets a fixed time quantum and cycles through the ready queue (preemptive).
- **Priority Scheduling:** Processes are executed based on assigned priority.
- **Starvation:** A process is indefinitely delayed from getting a resource or CPU time.
- **Aging:** Gradually increasing the priority of waiting processes to prevent starvation.
- **Synchronization:** Coordinating the execution of multiple processes or threads to access shared resources safely.
- **Race Condition:** A situation where the outcome depends on the unpredictable order of execution of multiple processes/threads accessing shared data.
- **Critical Section:** A code segment where a process accesses shared resources and must be executed exclusively.
- **Mutual Exclusion:** Only one process can be in its critical section at a time.
- **Progress:** If no process is in its critical section and some processes want to enter, only those not in their remainder sections can participate in the decision of which will enter next, and this selection cannot be postponed indefinitely.
- **Bounded Waiting:** There's a limit on the number of times other processes can enter their critical sections after a process has made a request to enter its critical section and before the request is granted.
- **Peterson's Solution:** A software-based solution to the critical section problem for two processes.
- **Semaphore:** A synchronization tool (integer variable) used to control access to shared resources and prevent race conditions.
- **Binary Semaphore (Mutex):** A semaphore that can only be 0 or 1, used for mutual exclusion (like a lock).
- **Counting Semaphore:** A semaphore that can take any non-negative integer value, used to manage multiple instances of a resource.
- **wait() (or P()):** Decrements the semaphore value; if the value becomes negative, the process blocks.
- **signal() (or V()):** Increments the semaphore value; if there are blocked processes, one is unblocked.
- **Deadlock:** A situation where two or more processes are blocked indefinitely, each waiting for a resource held by another.
- **Hold and Wait:** A deadlock condition where a process holds at least one resource while waiting for others.
- **No Preemption:** A deadlock condition where resources cannot be forcibly taken from a process.
- **Circular Wait:** A deadlock condition forming a circular chain of processes waiting for resources held by the next process in the chain.
- **Bounded Buffer Problem (Producer-Consumer Problem):** A synchronization problem involving a producer process adding items to a limited buffer and a consumer process removing items, requiring coordination.
- **Readers and Writers Problem:** A synchronization problem involving multiple readers and writers accessing a shared resource, allowing multiple readers simultaneously but only one writer at a time.
- **Dining Philosophers Problem:** A classic concurrency problem illustrating the challenges of resource allocation and the potential for deadlock and starvation when multiple processes compete for a limited number of resources.
- **Monitor:** A high-level synchronization construct (in some programming languages) providing mutual exclusion and condition variables within a structured module.
- **Resource Allocation Graph (RAG):** A directed graph used in deadlock detection and prevention, showing processes, resources, requests, and allocations.
- **Banker's Algorithm:** A deadlock avoidance algorithm that checks if a system can allocate resources safely without entering an unsafe state that could lead to deadlock.
- **Safe State:** A state where the system can allocate resources to all processes in some sequence without causing a deadlock.
- **Disk Scheduling:** The process of ordering disk I/O requests to minimize access time.
- **Seek Time:** The time taken for the disk's read/write head to move to the correct track.
- **Rotational Latency:** The time taken for the desired sector to rotate under the read/write head.
- **FCFS (First-Come, First-Served) Disk Scheduling:** Services disk requests in the order they arrive.
- **SSTF (Shortest Seek Time First):** Selects the request with the shortest seek time from the current head position.
- **SCAN (Elevator Algorithm):** The head moves in one direction, servicing requests along the way, then reverses direction.
- **C-SCAN (Circular SCAN):** The head moves in one direction, servicing requests, and when it reaches the end, it immediately moves back to the other end without servicing requests on the return trip.
- **LOOK:** Similar to SCAN but only moves to the farthest request in the current direction, then reverses.
- **C-LOOK:** Similar to C-SCAN but only moves to the farthest request in one direction and then immediately returns to the farthest request in the opposite direction.