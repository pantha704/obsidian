### Module-I: Overview

**1. Energy and Power Signals:**

- **Energy Signals:** Signals with finite energy, typically decaying over time. Energy is calculated as E=∫−∞∞∣x(t)∣2dtE = \int_{-\infty}^{\infty} |x(t)|^2 dtE=∫−∞∞​∣x(t)∣2dt for continuous signals and E=∑n=−∞∞∣x[n]∣2E = \sum_{n=-\infty}^{\infty} |x[n]|^2E=∑n=−∞∞​∣x[n]∣2 for discrete signals.
- **Power Signals:** Signals with finite power, often periodic. Power is calculated as P=lim⁡T→∞12T∫−TT∣x(t)∣2dtP = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} |x(t)|^2 dtP=limT→∞​2T1​∫−TT​∣x(t)∣2dt for continuous signals and P=lim⁡N→∞12N+1∑n=−NN∣x[n]∣2P = \lim_{N \to \infty} \frac{1}{2N+1} \sum_{n=-N}^{N} |x[n]|^2P=limN→∞​2N+11​∑n=−NN​∣x[n]∣2 for discrete signals.

**2. Continuous and Discrete Time Signals:**

- **Continuous Time Signals:** Defined for every instant of time ttt.
- **Discrete Time Signals:** Defined only at discrete times nnn.

**3. Continuous and Discrete Amplitude Signals:**

- **Continuous Amplitude Signals:** Amplitudes can take any value in a continuous range.
- **Discrete Amplitude Signals:** Amplitudes can only take values from a discrete set.

**4. System Properties:**

- **Linearity:** A system is linear if it satisfies superposition, meaning T{ax1(t)+bx2(t)}=aT{x1(t)}+bT{x2(t)}T\{a x_1(t) + b x_2(t)\} = a T\{x_1(t)\} + b T\{x_2(t)\}T{ax1​(t)+bx2​(t)}=aT{x1​(t)}+bT{x2​(t)}.
- **Shift-Invariance:** A system is shift-invariant if a shift in the input results in an identical shift in the output.
- **Causality:** A system is causal if the output at any time depends only on present and past inputs, not future inputs.
- **Stability:** A system is stable if bounded inputs always produce bounded outputs (BIBO stability).
- **Reliability:** Consistent performance and accuracy of a system over time.

This module lays the foundation for understanding different types of signals and their properties, which is crucial for analyzing and designing systems that process these signals.
