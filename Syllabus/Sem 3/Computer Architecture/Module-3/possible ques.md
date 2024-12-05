


Here are potential exam questions from Module-III on Memory Organization:

### Theoretical Questions:

1. **Memory Hierarchy**
- Explain the different levels of memory hierarchy and their characteristics.
- Compare and contrast cache memory and main memory.
- What are temporal and spatial locality? Give examples.

2. **Cache Coherence**
- Explain the cache coherence problem in multiprocessor systems.
- Describe the MSI and MESI protocols with state diagrams.
- What is snooping and how does it help maintain cache coherence?

3. **Virtual Memory**
- Explain paging and segmentation in virtual memory.
- Compare different page replacement policies (LRU, FIFO).
- How does virtual memory handle page faults?

### Numerical/Problem-Solving Questions:

1. **Cache Performance**
```
Given:
- Cache access time: 20ns
- Main memory access time: 100ns
- Cache hit ratio: 0.8
Calculate:
a) Average memory access time
b) System performance improvement compared to no cache
```

2. **Page Replacement**
```
Given page reference string: 1,2,3,4,1,2,5,1,2,3,4,5
Page frames available: 3
Calculate number of page faults using:
a) FIFO
b) LRU
```

3. **Memory Interleaving**
```
In a system with 4-way interleaved memory:
- Memory access time: 50ns
- Memory cycle time: 100ns
Calculate effective access time for:
a) Sequential access to 8 words
b) Random access to 8 words
```

### Sample Solutions:

1. **Cache Performance**
```
a) Average Access Time = Hit_Time + Miss_Ratio × Miss_Penalty
   = (0.8 × 20) + (0.2 × 120)
   = 16 + 24 = 40ns

b) Improvement = (100 - 40)/100 × 100%
   = 60% improvement
```

2. **Page Replacement (FIFO)**
```
Initial state: Empty frames
1: [1] - fault
2: [1,2] - fault
3: [1,2,3] - fault
4: [4,2,3] - fault (replace 1)
...and so on
```

### Important Topics to Focus On:
1. Memory hierarchy and its characteristics
2. Cache coherence protocols
3. Virtual memory management
4. Page replacement algorithms
5. Memory interleaving concepts
6. Access patterns and optimization

Would you like me to explain any of these questions or solutions in more detail?
