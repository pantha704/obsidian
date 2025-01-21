
Sure, I'll go through each problem and explain the concepts and solutions step by step.

### Problem 25:
Solve the following system of equations using Cramer's Rule:
\[ x + 3y - 4z = 0 \]
\[ 2x + 3y - z = 4 \]
\[ 4x - y + 2z = 5 \]

**Solution:**

Cramer's Rule states that for a system of linear equations \(AX = B\):
\[ AX = B \]

If \(A\) is the coefficient matrix and \(X = \begin{bmatrix} x \\ y \\ z \end{bmatrix}\), then:
\[ A = \begin{bmatrix} 1 & 3 & -4 \\ 2 & 3 & -1 \\ 4 & -1 & 2 \end{bmatrix}, \quad B = \begin{bmatrix} 0 \\ 4 \\ 5 \end{bmatrix} \]

To find \(x\), \(y\), and \(z\), we need to compute the determinants of \(A\), \(A_x\), \(A_y\), and \(A_z\):

1. Compute \(\det(A)\):
\[ \det(A) = \begin{vmatrix} 1 & 3 & -4 \\ 2 & 3 & -1 \\ 4 & -1 & 2 \end{vmatrix} \]

2. Compute \(\det(A_x)\), \(\det(A_y)\), and \(\det(A_z)\) by replacing the respective column with \(B\):

\[ A_x = \begin{bmatrix} 0 & 3 & -4 \\ 4 & 3 & -1 \\ 5 & -1 & 2 \end{bmatrix}, \quad A_y = \begin{bmatrix} 1 & 0 & -4 \\ 2 & 4 & -1 \\ 4 & 5 & 2 \end{bmatrix}, \quad A_z = \begin{bmatrix} 1 & 3 & 0 \\ 2 & 3 & 4 \\ 4 & -1 & 5 \end{bmatrix} \]

\[ x = \frac{\det(A_x)}{\det(A)}, \quad y = \frac{\det(A_y)}{\det(A)}, \quad z = \frac{\det(A_z)}{\det(A)} \]

Compute each determinant and substitute into the formulas to find \(x\), \(y\), and \(z\).

### Problem 26:
Find all the eigenvalues of the matrix:
\[ A = \begin{bmatrix} 1 & -1 & 2 \\ -2 & 4 & -1 \\ 3 & -3 & 6 \end{bmatrix} \]

**Solution:**

Eigenvalues are found by solving the characteristic equation:
\[ \det(A - \lambda I) = 0 \]

Where \(I\) is the identity matrix and \(\lambda\) are the eigenvalues.

\[ A - \lambda I = \begin{bmatrix} 1-\lambda & -1 & 2 \\ -2 & 4-\lambda & -1 \\ 3 & -3 & 6-\lambda \end{bmatrix} \]

Solve for the determinant and set it to zero:
\[ \det(A - \lambda I) = 0 \]

Solve this polynomial equation for \(\lambda\).

### Problem 27:
Define Hermitian and Skew-Hermitian matrices. Express the matrix \(A\) as the sum of a Hermitian and a skew-Hermitian matrix, where:
\[ A = \begin{bmatrix} 2 + 3i & 2 & 5 \\ -3 - i & 7 & 3 - i \\ 3 - 2i & i & 2 + i \end{bmatrix} \]

**Solution:**

- **Hermitian Matrix:** A matrix \(H\) is Hermitian if \(H = H^*\), where \(H^*\) is the conjugate transpose of \(H\).
- **Skew-Hermitian Matrix:** A matrix \(K\) is skew-Hermitian if \(K = -K^*\).

Any complex matrix \(A\) can be expressed as the sum of a Hermitian matrix \(H\) and a skew-Hermitian matrix \(K\):
\[ A = H + K \]
Where:
\[ H = \frac{A + A^*}{2}, \quad K = \frac{A - A^*}{2} \]

Compute \(A^*\) and then find \(H\) and \(K\).

### Problem 28:
Use the Gram-Schmidt process to find an orthogonal basis from the basis set \(\{(1, 2, 2), (2, -2, 1), (2, 1, -2)\}\) of \(\mathbb{R}^3\) with the standard inner product.

**Solution:**

1. Start with the first vector: \(v_1 = (1, 2, 2)\)
2. Orthogonalize the second vector \(v_2 = (2, -2, 1)\):
\[ u_2 = v_2 - \text{proj}_{v_1}(v_2) \]
3. Orthogonalize the third vector \(v_3 = (2, 1, -2)\):
\[ u_3 = v_3 - \text{proj}_{v_1}(v_3) - \text{proj}_{u_2}(v_3) \]

### Problem 29:
Use the Gram-Schmidt process to find an orthogonal basis from the basis set \(\{(1, 0, 1), (1, 1, 1), (1, 3, 4)\}\) of \(\mathbb{R}^3\) with the standard inner product.

**Solution:**

Follow the same steps as in Problem 28 with the given basis set.

### Problem 30:
Apply the Gram-Schmidt orthogonalization process to the set of vectors \(\{(1, 1, 1), (1, 0, 2), (0, 2, 1)\}\) to find an orthonormal set of vectors that is a basis for the vector space spanned by the given vectors.

**Solution:**

1. Start with the first vector: \(v_1 = (1, 1, 1)\)
2. Orthogonalize the second vector \(v_2 = (1, 0, 2)\):
\[ u_2 = v_2 - \text{proj}_{v_1}(v_2) \]
3. Orthogonalize the third vector \(v_3 = (0, 2, 1)\):
\[ u_3 = v_3 - \text{proj}_{v_1}(v_3) - \text{proj}_{u_2}(v_3) \]

Normalize the orthogonal vectors to get an orthonormal set.

### Problem 31:
Let \(T: \mathbb{R}^3 \to \mathbb{R}^3\) be the linear operator given by:
\[ T \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 3x_1 + x_2 \\ x_1 + x_3 \\ x_1 - x_3 \end{pmatrix} \]

Find the matrix for \(T\) with respect to the standard basis for \(\mathbb{R}^3\).

**Solution:**

Express \(T\) in terms of the standard basis vectors \(e_1, e_2, e_3\):
\[ T(e_1) = \begin{pmatrix} 3 \\ 1 \\ 1 \end{pmatrix}, \quad T(e_2) = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \quad T(e_3) = \begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix} \]

Form the matrix with these vectors as columns:
\[ T = \begin{pmatrix} 3 & 1 & 0 \\ 1 & 0 & 1 \\ 1 & 0 & -1 \end{pmatrix} \]

### Problem 32:
Let \(T: \mathbb{R}^3 \to \mathbb{R}^3\) be defined by:
\[ T(x_1, x_2, x_3) = (x_1 + x_2 + 3x_3, 2x_1 + 2x_2 + x_3, x_1 + 2x_2 + x_3) \]

Show that \(T\) is a linear map. Find \(\ker T\) and the dimension of \(\ker T\).

**Solution:**

- **Linearity:** Show \(T(ax + by) = aT(x) + bT(y)\) for scalars \(a, b\) and vectors \(x, y\).
- **Kernel:** Solve \(T(x_1, x_2, x_3) = 0\):
\[ x_1 + x_2 + 3x_3 = 0 \]
\[ 2x_1 + 2x_2 + x_3 = 0 \]
\[ x_1 + 2x_2 + x_

3 = 0 \]

Solve this system to find \(\ker T\).

### Problem 33:
Find the eigenvalues and corresponding eigenvectors of the following matrix:
\[ A = \begin{pmatrix} 1 & 2 & 3 \\ 0 & -2 & 6 \\ 0 & 0 & -3 \end{pmatrix} \]

**Solution:**

Find the characteristic polynomial and solve for the eigenvalues \(\lambda\). Then, find the corresponding eigenvectors for each \(\lambda\).

### Problem 34:
Solve the following system of equations using the LU decomposition method:
\[ x + y - z = 4 \]
\[ x - 2y + 3z = -6 \]
\[ 2x + 3y + z = 7 \]

**Solution:**

1. Write the system in matrix form \(AX = B\):
\[ A = \begin{pmatrix} 1 & 1 & -1 \\ 1 & -2 & 3 \\ 2 & 3 & 1 \end{pmatrix}, \quad B = \begin{pmatrix} 4 \\ -6 \\ 7 \end{pmatrix} \]

2. Perform LU decomposition on \(A\) to get \(L\) and \(U\):
\[ A = LU \]

3. Solve \(LY = B\) for \(Y\).
4. Solve \(UX = Y\) for \(X\).

By following these explanations, you should be able to solve each problem in detail. Good luck with your exam!