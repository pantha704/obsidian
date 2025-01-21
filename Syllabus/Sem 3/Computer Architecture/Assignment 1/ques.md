
[1] What is Processor Performance Equation?
[2] What is Amdahl’s Law? Write down the Equation.
[3] Explain Pipeline speed up Equation.
[4] What is pipelining? Explain properly.
[5] What are different factors that can affect pipeline system?
[6] Explain difference between RISC and CISC with proper diagram.
[7] Suppose that we want to enhance the processor used for Web serving. The 
new processor is 10 times faster on computation in the Web serving 
application than the original processor. Assuming that the original processor 
is busy with computation40% of the time and is waiting for I/O 60% of the 
time, what is the overall speedup gained by incorporating the enhancement?
[8] Write down the relation between CPI and Instruction Count.
[9] Write down the formula for Overall CPI where numbers of Instructions varies 
from 1 to n.
[10] A common transformation required in graphics engines is square root. 
Implementations of floating-point (FP) square root vary significantly in 
performance, especially among processor designed for graphics. Suppose
FP square root (FPSQR) is responsible for 20% of the execution time of a 
critical graphics benchmark. One proposal is to enhance the FPSQR
hardware and speed up this operation by a factor of 10. The other 
alternative is just to try to make all FP instructions in the graphics 
processor run faster by a factor of 1.6; FP instructions are responsible for a 
total of 50% of the execution time for the application. The design team 
believes that they can make all FP instructions run 1.6 times faster with 
the same effort as required for the fast square root. Compare these two 
design alternatives.
[11] What is Pipelining Hazards? Explain Different types of Hazards.
[12] Explain Structural Hazards? And also explain how to resolve this using 
diagram.
[13] Explain Data Hazards? And also explain how to resolve this using 
diagram.
[14] Explain Control Hazards? And also explain how to resolve this using 
diagram.
[15] Explain Different types of Data Hazards using examples.
[16] Assume there is 5-stage pipeline structure, and each stage is taking 1 
clock cycle. Find out clock cycles are required to complete the instruction
set. And also identify the different types of data hazards.
MUL R1, R2, R3
DIV R4, R1, R6
ADD R7, R4, R8
SUB R9, R2, R6
[17] (a) Assume there is 5-stage pipeline structure, and each stage is taking 1 
clock cycle. Find out clock cycles are required to complete the instruction 
set. And also identify the different types of data hazards.
MUL R1, R2, R3
DIV R4, R1, R5
ADD R6, R1, R7
SUB R8, R6, R9
XOR R10, R1, R11
(b) If you are using operand forwarding techniques, find out clock cycles 
are required to complete the instruction set. And also identify the different 
types of data hazards. And compare the clock cycles for both cases.
[18] What is delayed slot in Control hazards?
[19] Explain different Pipelining performance parameters.
[20] Define Speed-up, Efficiency, and Throughput. Write down the formula for 
each case.
[21] Consider the following Computer:-
Code type- A (1 cycle) B (2 cycle) C (3 cycle)
Compiler 1 5 1 1
Compiler 2 10 1 1
Instruction A requires 1 clock cycle, Instruction B requires 2 clock cycles, 
Instruction C requires 3 clock cycles.
The machine runs at 100 MHz. 
(a) Find out MIPS for both the cases. And compare.
(b) Compare CPU time for both the cases.
[22] Consider an unpipelined processor:
Takes 4 cycles for ALU and other operations; 5 cycles for memory 
operations.
Assume the relative frequencies:
ALU and other=60%; memory operations=40%; Cycle time =1ns
Compute speedup due to pipelining:
Ignore effects of branching.
Assume pipeline overhead = 0.2ns
Find:
(a) Compare Average instruction execution time for unpipelining and 
pipelined cases.
(b) What will be speed up value while using pipelining?
[23] Consider one 5-Stage pipelining Structure, where 12 numbers of 
Instructions are there; and pipeline cycle time is 2 Microseconds. Find out
(a) Speed up
(b) Efficiency
(c) Throughput
[24] Make a proper difference between Arithmetic pipeline and Instruction 
Pipeline.
[25] Explain (a) Input Interface workflow (b) Output Interface workflow.