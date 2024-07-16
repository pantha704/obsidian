
### Module-V: Overview

**1. z-Transform:**
   - **Definition:**
     \[
     \mathcal{Z}\{x[n]\} = X(z) = \sum_{n=-\infty}^{\infty} x[n] z^{-n}
     \]
   - **Properties:** Linearity, time shifting, frequency shifting, differentiation in the z-domain, convolution in the time domain.

**2. Eigen Functions in Discrete Systems:**
   - **Eigen Functions:** In discrete systems, the eigen functions are complex exponentials \(z^n\).
   - **Eigenvalues:** For a discrete-time linear time-invariant (LTI) system, the response to \(z^n\) is scaled by the system function \(H(z)\).

**3. Region of Convergence (ROC):**
   - **ROC:** The set of \(z\)-values for which the z-transform converges.
   - **Properties:** Determines the causality and stability of the system, and depends on the type of signal (right-sided, left-sided, two-sided).

**4. z-Domain Analysis:**
   - **System Function \(H(z)\):**
     \[
     H(z) = \frac{Y(z)}{X(z)}
     \]
     where \(Y(z)\) is the z-transform of the output and \(X(z)\) is the z-transform of the input.
   - **Poles and Zeros:** 
     - **Poles:** Values of \(z\) that make \(H(z)\) go to infinity.
     - **Zeros:** Values of \(z\) that make \(H(z)\) equal to zero.
   - **Significance:** Poles and zeros determine the system's frequency response and stability. Poles within the unit circle indicate stability.

**5. z-Domain Analysis of Systems:**
   - **Difference Equations:** Use the z-transform to solve linear difference equations by converting them to algebraic equations in the z-domain.
   - **Example:**
     For the difference equation:
     \[
     y[n] - 0.5y[n-1] = x[n]
     \]
     Taking the z-transform:
     \[
     Y(z) - 0.5z^{-1}Y(z) = X(z)
     \]
     Solve for \(Y(z)\):
     \[
     Y(z) = \frac{X(z)}{1 - 0.5z^{-1}}
     \]
     Perform inverse z-transform to find \(y[n]\).

**6. System Behavior Analysis:**
   - **Stability:** Determined by the location of poles in the z-domain. A discrete system is stable if all poles lie inside the unit circle in the z-plane.
   - **Transient and Steady-State Response:** Poles and zeros influence how the system responds over time and reaches a steady state.

This module focuses on using the z-transform as a tool for analyzing discrete-time signals and systems. It is analogous to the Laplace transform for continuous-time systems but is specifically tailored for discrete-time systems. The z-transform simplifies the analysis of difference equations and provides insights into system behavior, including stability and frequency response, through the use of poles, zeros, and the region of convergence.