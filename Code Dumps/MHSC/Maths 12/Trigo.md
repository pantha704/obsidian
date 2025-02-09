
Below is a beginner-friendly explanation that breaks down the three topics—**Mathematical Logic**, **Matrices**, and **Trigonometric Functions**—into simpler parts. Take your time with each section and try to work through small examples as you read along.

---

# 1. Mathematical Logic

Mathematical logic helps us think clearly by using precise language and rules to tell whether a statement is true or false.

### **A. Statements and Truth Values**

- **Statement:**  
  A sentence that can be clearly identified as either _true_ or _false_.  
  **Examples:**  
  - "The sun rises in the East." (True)  
  - "Every triangle has three sides." (True)  
  - "Mumbai is the capital of Maharashtra." (False; it is Mumbai's status vs. the actual capital, which is Mumbai's state capital is Mumbai anyway in this case, but you get the idea with a false statement example)

- **Non-Statements:**  
  These include questions, commands, or sentences whose truth relies on a variable (for example, "x + 6 = 9" cannot be decided until you specify what x is).

- **Truth Values:**  
  Every statement is either **True (T)**, or **False (F)**.

---

### **B. Logical Connectives and Compound Statements**

Often, we need to combine simple statements into more complex ones using special words called **logical connectives**:

- **AND (∧):**  
  - _Meaning:_ Both parts must be true.  
  - _Example:_ "It is raining **and** it is cold." (True only if both "it is raining" **and** "it is cold" are true.)

- **OR (∨):**  
  - _Meaning:_ At least one part must be true.  
  - _Example:_ "I will have tea **or** coffee." (If either or both are true, the statement is true.)

- **IF...THEN (→):**  
  - _Meaning:_ Tells you that if the first part (the condition) is true, then the second must be true.  
  - _Example:_ "If it rains, then the ground gets wet."  
    (This statement is false only if it is raining and the ground is not wet.)

- **IF AND ONLY IF (↔):**  
  - _Meaning:_ Both sides must have the same truth value.  
  - _Example:_ "You can enter **if and only if** you have a ticket."  
    (This means having a ticket and being allowed entry always go together.)

- **NOT (¬):**  
  - _Meaning:_ Reverses the truth value (turns true into false; false into true).  
  - _Example:_ "It is not raining" is the negation of "It is raining."

---

### **C. Truth Tables**

A truth table lists all possible combinations of truth values for simple statements and shows the outcome for compound statements.

#### **Example: Conjunction (AND, ∧)**

| p   | q   | p ∧ q |
| --- | --- | ----- |
| T   | T   | T     |
| T   | F   | F     |
| F   | T   | F     |
| F   | F   | F     |

This table shows that "p and q" is only true when both p and q are true.

---

### **D. Logical Equivalence, Tautology, Contradiction, and Other Laws**

- **Logical Equivalence:**  
  Two statement forms (patterns) are equivalent if their truth tables are exactly the same—written as A ≡ B.

- **Tautology:**  
  A compound statement that is always true, no matter the truth values of its parts.  
  _Example:_ "p or not p" is always true.

- **Contradiction:**  
  A compound statement that is always false.  
  _Example:_ "p and not p" is always false.

- **Contingency:**  
  A statement that may be true in some cases and false in others.

- **Key Logical Laws:**  
  These are rules for simplifying compound statements, similar to algebra rules. For example:  
  - **Commutative Law:** p ∧ q is the same as q ∧ p (the order doesn’t matter).  
  - **Associative Law:** p ∧ (q ∧ r) is the same as (p ∧ q) ∧ r.  
  - **Distributive Law:** p ∧ (q ∨ r) is the same as (p ∧ q) ∨ (p ∧ r).  
  - **De Morgan’s Laws:**  
    - ¬(p ∧ q) is equivalent to ¬p ∨ ¬q.  
    - ¬(p ∨ q) is equivalent to ¬p ∧ ¬q.

- **Converse, Inverse, and Contrapositive:**  
  For an implication, "if p, then q" (p → q):  
  - **Converse:** "if q, then p" (q → p).  
  - **Inverse:** "if not p, then not q" (¬p → ¬q).  
  - **Contrapositive:** "if not q, then not p" (¬q → ¬p).  
  _Note:_ The original statement and its contrapositive are always logically equivalent.

---

# 2. Matrices

Matrices are a way to organize numbers into a rectangular array. They are useful for solving systems of equations, among other things.

### **A. What Is a Matrix?**

- **Matrix:**  
  A grid of numbers arranged in rows and columns.  
  **Example:**  
  \[
  \begin{bmatrix}
  1 & 2 & 3 \\
  4 & 5 & 6
  \end{bmatrix}
  \]
  This is a **2×3 matrix** (2 rows and 3 columns).

- **Square Matrix:**  
  A matrix with the same number of rows and columns (like a 3×3 matrix).

---

### **B. Elementary Transformations (Row Operations)**

Elementary transformations are simple operations you can perform on a matrix without changing its overall solution properties:

1. **Row Interchange (Switching Rows):**  
   Swap two rows.  
   _Example:_ Swap Row 1 with Row 2.

2. **Scalar Multiplication:**  
   Multiply every element of a row (or a column) by a nonzero number.  
   _Example:_ Multiply Row 1 by 2.

3. **Row Addition:**  
   Add a multiple of one row to another row.  
   _Example:_ Replace Row 2 with (Row 2 + 3 × Row 1).

These operations are the backbone of methods like **Gaussian elimination**, which is used to solve systems of linear equations.

---

### **C. Inverse of a Matrix**

- **Inverse Matrix (A⁻¹):**  
  For a square matrix A, its inverse is another matrix such that:  
  \[
  A \times A^{-1} = A^{-1} \times A = I,
  \]
  where I is the identity matrix (a matrix with 1s on the diagonal and 0s elsewhere).

- **When It Exists:**  
  A matrix has an inverse only if its **determinant** is not zero (such a matrix is called non-singular).

- **Finding the Inverse:**  
  - **Row Operations Method:** Use elementary transformations to convert A to I, doing the same to an identity matrix which will then become A⁻¹.  
  - **Adjoint Method:** Calculate cofactors for each element, form the cofactor matrix, transpose it to get the adjoint, and then use the formula:  
    \[
    A^{-1} = \frac{1}{\det(A)} \text{adj}(A).
    \]

---

### **D. Applications of Matrices**

- **Solving Systems of Equations:**  
  If you have a system written as AX = B and if A⁻¹ exists, you can find the solution by computing:  
  \[
  X = A^{-1}B.
  \]

- **Other Uses:**  
  Matrices are used in computer graphics, physics, statistics, and many other fields.

---

# 3. Trigonometric Functions

Trigonometry deals with relationships between the angles and sides of triangles and the periodic behavior of trigonometric functions like sine, cosine, and tangent.

### **A. Trigonometric Equations and Solutions**

- **Trigonometric Equations:**  
  These are equations that involve trigonometric functions.  
  **Examples:**  
  - sin θ = 1/2  
  - cos θ = 0.  
  A **solution** is a value of θ (angle) that makes the equation true.

- **Principal vs. General Solutions:**  
  - **Principal Value:**  
    A solution within a standard interval, usually 0 ≤ θ < 2π (or 0° to 360°).  
    _Example:_ sin θ = 1/2 has principal solutions of θ = π/6 and θ = 5π/6.
  - **General Solution:**  
    Because trigonometric functions are periodic, there are infinitely many solutions. For example:  
    - The general solution of sin θ = sin α is:  
      \[
      θ = nπ + (-1)^n α \quad \text{(with } n \text{ being any integer)}
      \]

---

### **B. Important Formulas for Triangles**

- **Sine Rule:**  
  In any triangle ∆ABC, the ratio of a side to the sine of its opposite angle is the same for all sides:  
  \[
  \frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R,
  \]
  where R is the circumradius (radius of the circle passing through all vertices).

- **Cosine Rule:**  
  Relates the sides of a triangle with one of its angles:  
  \[
  a^2 = b^2 + c^2 - 2bc \cos A.
  \]
  (Similar formulas exist for b² and c².)

- **Projection Rule:**  
  Relates the sides and angles using projections.  
  _Example:_  
  \[
  a = b \cos C + c \cos B.
  \]

- **Heron’s Formula (for area):**  
  If the sides of a triangle are a, b, c and the semiperimeter is s = (a + b + c)/2, then:  
  \[
  \text{Area} = \sqrt{s(s-a)(s-b)(s-c)}.
  \]

---

### **C. Inverse Trigonometric Functions**

Trigonometric functions are not one-to-one (they repeat), meaning they do not have inverses unless we restrict their domains. The inverses help us “undo” a trigonometric function.

- **Inverse Sine (sin⁻¹):**  
  Domain: [-1, 1]  
  Range: [ -π/2, π/2 ]
- **Inverse Cosine (cos⁻¹):**  
  Domain: [-1, 1]  
  Range: [0, π]
- **Inverse Tangent (tan⁻¹):**  
  Domain: All real numbers  
  Range: ( -π/2, π/2 )

These inverses allow you to find the angle when you know the value of the sine, cosine, or tangent.

---

### **D. Other Useful Trigonometric Formulas**

- **Half-Angle Formulas:**  
  They express sine, cosine, and tangent of half an angle in terms of the sides of the triangle (often using the semiperimeter s).

- **Napier’s Analogy:**  
  A formula that relates the differences and sums of sides and angles in a triangle, useful in some trigonometric calculations.

- **Key Identities:**  
  Relationships like sin²θ + cos²θ = 1 help simplify trigonometric expressions.

---

# Recap

- **Mathematical Logic** tells you how to construct and analyze statements (or assertions) using precise rules and tools like truth tables.  
- **Matrices** organize numbers in a grid format and allow you to solve equations and perform other calculations by using simple operations (like swapping rows or multiplying by constants).  
- **Trigonometric Functions** help you understand the properties of triangles and the periodic behavior of angles, which is valuable in geometry and many practical applications.

---

Remember, the best way to learn these topics is to practice:  
- Start with simple examples and build up to more complex problems.  
- Work through truth tables and practice re-arranging matrices with elementary operations.  
- Draw triangles, label the sides and angles, and apply the sine and cosine rules.

If any particular part is confusing, you can ask targeted questions or focus on one section at a time. Happy learning!
