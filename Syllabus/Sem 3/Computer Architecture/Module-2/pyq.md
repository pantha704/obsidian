

Sure, here are the answers:

### (i) MIPS means
- **(b) Million Instructions Per Second**

### (ii) A pipeline stage
- **(c) consists of both sequential and combinational circuits**

### (iii) Utilization pattern of successive stages of a synchronous pipeline can be specified by
- **(c) Reservation Table**

### (iv) Which of the following is not a RISC architecture characteristic?
- **(d) Small register file**: RISC architectures typically have a large register file.

### (v) Which of the following architectures corresponds to von-Neumann?
- **(c) SISD**: Single Instruction, Single Data is the classic von-Neumann architecture.

### (vi) Which of the following is not the cause of possible data hazard?
- **(a) RAR**: Read After Read is not a data hazard.

### (vii) In associative mapping, in a 16-bit system the tag field has _____ bits.
- **(b) 8**: This depends on the specific cache configuration, but typically, the tag size is determined by the number of index and offset bits.

### (viii) VLIW stands for?
- **(a) Very Long Instruction Word**

### (ix) In which type of memory mapping there will be conflict miss?
- **(a) Direct mapping**: Conflict misses occur when multiple data blocks map to the same cache line.

### (x) The number of cycles required to complete n tasks in a k stage pipeline is
- **(b) Nk+1**: This is a typical formula for calculating cycles in a pipeline.

### Group B: Explain Different types of Data Hazards using examples.
- **RAW (Read After Write)**: Occurs when an instruction needs data that hasn't been written back yet.
- **WAW (Write After Write)**: Occurs when two instructions write to the same location.
- **WAR (Write After Read)**: Occurs when an instruction writes to a location before a previous instruction reads it.

### Group C: Amdahl’s Law
- **(a) Explanation**: Amdahl's Law is used to find the maximum improvement in performance of a task when only part of the task can be improved.
- **(b) Speedup Calculation**: 
  - Original time: 40% computation, 60% I/O.
  - New computation time: 10 times faster.
  - Speedup = 1 / [(0.4/10) + 0.6] = 1 / [0.04 + 0.6] = 1 / 0.64 ≈ 1.56

### Group C: Pipeline Speedup and Efficiency
- **Speedup**: Speedup = (Number of stages) / (1 + Pipeline stalls)
- **Efficiency**: Efficiency = (Speedup / Number of stages) * 100%

If you need further details or explanations, feel free to ask!
