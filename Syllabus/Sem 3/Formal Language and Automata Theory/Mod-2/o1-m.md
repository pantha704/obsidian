
# Module-II: Finite Automation [10L]

This comprehensive guide covers the essential topics of **Module-II: Finite Automation**, focusing on number representations and computer arithmetic. This resource is designed to help you prepare effectively for your exam by providing clear and detailed explanations of each topic.

---

## 1. Signed Number Representation, Fixed and Floating Point Representations, Character Representation

### **Signed Number Representation**

Signed numbers allow the representation of both positive and negative integers in binary systems. There are several methods to represent signed numbers:

#### **a. Sign-Magnitude Representation**
- **Structure**: The first bit represents the sign (0 for positive, 1 for negative). The remaining bits represent the magnitude.
- **Example**: 
  - +5: `0 0101`
  - -5: `1 0101`
- **Advantages**: Simple and intuitive.
- **Disadvantages**: Two representations of zero (`+0` and `-0`), complicating arithmetic operations.

#### **b. One’s Complement Representation**
- **Structure**: Negative numbers are obtained by inverting all bits of the positive number.
- **Example**:
  - +5: `0101`
  - -5: `1010` (inversion of `0101`)
- **Advantages**: Easier arithmetic operations compared to sign-magnitude.
- **Disadvantages**: Still has two representations of zero, leading to complexity.

#### **c. Two’s Complement Representation**
- **Structure**: Negative numbers are obtained by inverting all bits of the positive number and adding 1.
- **Example**:
  - +5: `0101`
  - -5: `1011` (inversion of `0101` is `1010`; adding 1 gives `1011`)
- **Advantages**: Only one representation of zero, simplifies arithmetic operations.
- **Disadvantages**: Slightly less intuitive than sign-magnitude.

**Why Two’s Complement?**
Two’s complement is preferred in modern computing because it simplifies the design of arithmetic circuits and eliminates the issue of having two zeros.

---

### **Fixed and Floating Point Representations**

#### **a. Fixed-Point Representation**
- **Definition**: Numbers are represented with a fixed number of bits for the integer and fractional parts.
- **Structure**: `[Sign][Integer Bits].[Fractional Bits]`
- **Example**:
  - Format: `IIII.FFFF` (4 integer bits and 4 fractional bits)
  - Number: `+3.75` → `0011.1100`
- **Advantages**:
  - Simpler hardware implementation.
  - Predictable precision and range.
- **Disadvantages**:
  - Limited range and precision.
  - Not suitable for very large or very small numbers.

#### **b. Floating-Point Representation**
- **Definition**: Numbers are represented with a mantissa (significand) and an exponent, allowing for a wide range of values.
- **Structure**: `(-1)^s × 1.M × 2^(E-Bias)`
  - **s**: Sign bit
  - **M**: Mantissa (with an implicit leading 1)
  - **E**: Exponent
  - **Bias**: A constant added to the exponent for representation
- **IEEE 754 Standard**:
  - **Single Precision**: 1 sign bit, 8 exponent bits, 23 mantissa bits
  - **Double Precision**: 1 sign bit, 11 exponent bits, 52 mantissa bits
- **Advantages**:
  - Wide range of representable numbers.
  - Efficient use of bits for varying magnitudes.
- **Disadvantages**:
  - More complex hardware implementation.
  - Precision issues due to rounding.

---

### **Character Representation**

Characters are represented in binary systems using standardized encoding schemes. The most common representations are:

#### **a. ASCII (American Standard Code for Information Interchange)**
- **Structure**: 7-bit encoding, extended to 8 bits in modern systems.
- **Range**: 0 to 127 (standard ASCII), 128 to 255 (extended ASCII)
- **Example**:
  - 'A': `01000001` (65)
  - 'a': `01100001` (97)
- **Advantages**: Simple and widely adopted.
- **Disadvantages**: Limited to English characters.

#### **b. Unicode**
- **Structure**: Variable-length encoding (UTF-8, UTF-16, UTF-32)
- **Range**: Supports millions of characters from various languages and symbols.
- **Example**:
  - '😊': `F09F988A` (UTF-8)
- **Advantages**: Comprehensive representation of global characters.
- **Disadvantages**: More complex and requires more storage space.

---

## 2. Computer Arithmetic

Computer arithmetic deals with the methods and algorithms used to perform arithmetic operations within a computer. This section covers integer addition and subtraction, various adder designs, multiplication techniques, division algorithms, and floating-point arithmetic.

### **a. Integer Addition and Subtraction**

#### **Addition**
- **Binary Addition Rules**:
  - `0 + 0 = 0`
  - `0 + 1 = 1`
  - `1 + 0 = 1`
  - `1 + 1 = 0` (carry 1)
- **Example**: Adding `0110` (+6) and `0011` (+3)
  ```
    0110
  + 0011
  -------
    1001 (+9)
  ```

#### **Subtraction**
- **Method**: Use two’s complement.
- **Steps**:
  1. Find the two’s complement of the number to be subtracted.
  2. Add it to the first number.
  3. Ignore any carry out.
- **Example**: Subtracting `0011` (+3) from `0110` (+6)
  ```
    0110
  - 0011
  -------
    0011 (+3)
  ```

### **b. Ripple Carry Adder**

- **Definition**: A simple type of adder where each bit addition is processed sequentially, with each carry bit "rippling" to the next higher bit.
- **Structure**:
  ```
    Cin ---> [Full Adder 0] ---> Cout0 ---> [Full Adder 1] ---> Cout1 ---> ...
  ```
- **Advantages**:
  - Simple to implement.
- **Disadvantages**:
  - Slow for large bit-widths due to sequential carry propagation.

### **c. Carry Look-Ahead Adder**

- **Definition**: An advanced adder that improves speed by calculating carry bits in advance, based on input bits.
- **Concept**:
  - Use generate (`G`) and propagate (`P`) signals.
  - `G = A AND B`
  - `P = A XOR B`
- **Carry Calculation**:
  ```
  C1 = G0 OR (P0 AND C0)
  C2 = G1 OR (P1 AND G0) OR (P1 AND P0 AND C0)
  ...
  ```
- **Advantages**:
  - Faster than ripple carry adders.
- **Disadvantages**:
  - More complex circuitry.

### **d. Multiplication**

#### **i. Shift-and-Add Method**
- **Procedure**:
  1. Initialize the result to 0.
  2. For each bit in the multiplier:
     - If the bit is 1, add the multiplicand shifted by the bit's position to the result.
     - Shift the multiplicand left by one bit.
  3. Repeat until all bits are processed.
- **Example**: Multiply `5 (0101)` by `3 (0011)`
  ```
    0101 (5)
  x 0011 (3)
  -------
    0101   (5 x 1)
   0101    (5 x 1, shifted left by 1)
  -------
    1111   (15)
  ```

#### **ii. Booth Multiplier**
- **Concept**: Reduces the number of addition operations by encoding the multiplier using Booth's algorithm.
- **Procedure**:
  1. Examine pairs of bits in the multiplier.
  2. Perform addition or subtraction based on the bit transitions.
  3. Shift the partial product accordingly.
- **Advantages**:
  - More efficient for multipliers with consecutive 1s or 0s.
- **Disadvantages**:
  - More complex than shift-and-add.

#### **iii. Carry Save Multiplier**
- **Concept**: Handles multiple additions simultaneously by saving carry bits separately.
- **Procedure**:
  1. Convert each partial product into a carry-save form.
  2. Use carry-save adders to accumulate partial products.
  3. Finalize the result using a conventional adder.
- **Advantages**:
  - Faster for large multipliers by reducing the number of required adders.
- **Disadvantages**:
  - Requires additional circuitry to manage carry bits.

### **e. Division**

#### **i. Restoring Division**
- **Procedure**:
  1. Initialize the remainder to 0.
  2. For each bit in the dividend:
     - Shift the remainder left and bring down the next bit.
     - Subtract the divisor from the remainder.
     - If the remainder is negative, restore it by adding the divisor and set the quotient bit to 0.
     - Otherwise, set the quotient bit to 1.
  3. Repeat until all bits are processed.
- **Advantages**:
  - Simple to implement.
- **Disadvantages**:
  - May require more operations due to restoring step.

#### **ii. Non-Restoring Division**
- **Procedure**:
  1. Similar to restoring division but avoids the restorative step by keeping track of the sign.
  2. Based on the sign of the partial remainder, decide whether to subtract or add the divisor.
- **Advantages**:
  - Faster than restoring division as it eliminates the restore step.
- **Disadvantages**:
  - More complex to manage the sign of the partial remainder.

### **f. Floating Point Arithmetic**

Floating-point arithmetic involves operations on numbers with fractional components, represented in floating-point format. Performing arithmetic with floating-point numbers requires handling the mantissa and exponent separately.

#### **Addition and Subtraction**
1. **Align Exponents**: Shift the mantissa of the number with the smaller exponent to match the larger exponent.
2. **Add/Subtract Mantissas**: Perform the operation on the aligned mantissas.
3. **Normalize Result**: Adjust the result to maintain the normalized form.
4. **Handle Rounding**: Apply rounding to fit the mantissa into the allotted bits.

#### **Multiplication**
1. **Multiply Mantissas**: Multiply the significands of both numbers.
2. **Add Exponents**: Sum the exponents and adjust for the bias.
3. **Normalize Result**: Ensure the mantissa is in normalized form.
4. **Handle Overflow/Underflow**: Adjust for any exponent overflow or underflow.

#### **Division**
1. **Divide Mantissas**: Divide the significands of the numerator and denominator.
2. **Subtract Exponents**: Subtract the exponent of the denominator from the exponent of the numerator.
3. **Normalize Result**: Adjust the mantissa to maintain normalization.
4. **Handle Rounding and Special Cases**: Apply rounding and manage exceptions like division by zero.

**Key Considerations**:
- **Precision**: Limited number of bits can lead to rounding errors.
- **Normalization**: Ensures consistent representation by maintaining leading 1 in the mantissa.
- **Rounding Modes**: Methods like round-to-nearest, round-up, and round-down to handle precision limits.

---

## Summary

Understanding number representations and computer arithmetic is fundamental to computer science and engineering. 

- **Signed Number Representations** like two’s complement simplify arithmetic operations and hardware design.
- **Fixed and Floating-Point Representations** provide different trade-offs between range and precision, with floating-point being essential for scientific computations.
- **Character Representations** like ASCII and Unicode enable the encoding of text data in computers.
- **Computer Arithmetic** encompasses a variety of algorithms and hardware designs to perform efficient arithmetic operations, vital for processor performance and accuracy.

Mastering these concepts will enhance your ability to design and analyze digital systems, optimize performance, and ensure accurate computations in software and hardware applications.

---

## Additional Tips for Exam Preparation

- **Practice Binary Operations**: Regularly perform binary additions, subtractions, and multiplications to build proficiency.
- **Understand Algorithms**: Grasp the step-by-step processes of algorithms like Booth’s multiplier and non-restoring division.
- **Draw Diagrams**: Visualize adder circuits and multiplication/division steps to reinforce understanding.
- **Solve Problems**: Work on a variety of problems covering different representations and arithmetic operations.
- **Review Special Cases**: Pay attention to edge cases in floating-point arithmetic, such as overflow, underflow, and NaN handling.

Good luck with your exam!
