Here are potential exam questions from Module-V on Multiprocessor Architecture:

### Theoretical Questions:

1. **Flynn's Taxonomy**
- Explain Flynn's taxonomy and its classification of computer architectures.
- Compare and contrast SIMD and MIMD architectures with examples.
- What are the key differences between shared memory and distributed memory systems?

2. **Memory Architecture**
- Explain the challenges in centralized shared-memory architectures.
- How does distributed shared-memory solve scalability issues?
- Describe various synchronization mechanisms in shared memory systems.

3. **Cluster Computing**
- What are the different types of computer clusters?
- Explain the advantages and challenges of cluster computing.
- How do high-availability clusters ensure continuous operation?

### Application/Numerical Questions:

1. **Memory Access Time**
```
Given:
- Local memory access time: 10ns
- Remote memory access time: 100ns
- Local access probability: 80%
Calculate:
a) Average memory access time
b) Performance impact compared to local-only access
```

2. **Cluster Performance**
```
For a cluster with:
- 8 nodes
- Each node: 4 cores, 3 GHz
- Network latency: 0.5ms
Calculate:
a) Total theoretical FLOPS
b) Effective performance with 20% communication overhead
```

3. **Synchronization Analysis**
```
Consider a critical section accessed by 4 processors:
- Critical section execution time: 100 cycles
- Lock acquisition time: 10 cycles
Calculate:
a) Best-case throughput
b) Worst-case throughput with contention
```

### Design Questions:

1. **System Design**
```
Design a distributed system for:
- Real-time stock trading
- Must handle 1000 transactions/second
- Maximum latency: 100ms
Specify:
a) Architecture type (Flynn's classification)
b) Memory organization
c) Synchronization mechanism
```

2. **Cluster Configuration**
```
Design a high-availability cluster for:
- Web application serving 1M users
- 99.99% uptime requirement
- Budget constraint: $100,000
Provide:
a) Number and type of nodes
b) Load balancing strategy
c) Failover mechanism
```

### Important Topics to Focus On:
1. Flynn's taxonomy and its applications
2. Memory organization in multiprocessor systems
3. Synchronization mechanisms
4. Cluster architectures and their uses
5. Performance calculations and metrics

Example code snippet showing synchronization:
```c
pthread_mutex_t lock;

void critical_section() {
    pthread_mutex_lock(&lock);    // Acquire lock
    // Perform thread-safe operations
    pthread_mutex_unlock(&lock);  // Release lock
}
```

Would you like me to explain any of these questions or provide detailed solutions?
