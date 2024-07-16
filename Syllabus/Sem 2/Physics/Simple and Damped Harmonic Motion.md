
### Simple Harmonic Motion (SHM)

1. **Find out the differential equation of simple harmonic motion and solve the equation. (4.1, 4.1.2)**
   - The differential equation for simple harmonic motion (SHM) is:
     \[ \frac{d^2x}{dt^2} + \omega^2 x = 0 \]
     where \( \omega \) is the angular frequency.
     - **Solution**: The general solution is:
       \[ x(t) = A \cos(\omega t + \phi) \]
       where \( A \) is the amplitude, and \( \phi \) is the phase constant.

2. **Write characteristics of simple harmonic motion.**
   - Characteristics of SHM include:
     - Periodic motion.
     - Restoring force proportional to displacement.
     - Sinusoidal displacement, velocity, and acceleration.
     - Constant amplitude and period.

3. **Define: Amplitude, frequency, time period.**
   - **Amplitude (A)**: The maximum displacement from the equilibrium position.
   - **Frequency (f)**: The number of oscillations per unit time.
   - **Time period (T)**: The time taken for one complete oscillation.

4. **Find amplitude, time period, frequency, and phase as given in class tests and assignments.**
   - **Amplitude (A)**: The peak value of the displacement.
   - **Time period (T)**: \( T = \frac{2\pi}{\omega} \)
   - **Frequency (f)**: \( f = \frac{1}{T} = \frac{\omega}{2\pi} \)
   - **Phase (\(\phi\))**: The initial angle at \( t = 0 \) in the SHM equation.

5. **Find the expression for the total energy in SHM. (4.2.4, 4.2.5)**
   - Total energy (E) in SHM:
     \[ E = \frac{1}{2}kA^2 = \frac{1}{2}m\omega^2A^2 \]
     where \( k \) is the spring constant, \( m \) is the mass, and \( \omega \) is the angular frequency.

6. **Plot kinetic energy and potential energy as a function of displacement. (Fig. 4.1)**
   - **Kinetic Energy (KE)**: \( KE = \frac{1}{2}mv^2 = \frac{1}{2}m\omega^2 (A^2 - x^2) \)
   - **Potential Energy (PE)**: \( PE = \frac{1}{2}kx^2 = \frac{1}{2}m\omega^2 x^2 \)
   - As a function of displacement \( x \), KE and PE are parabolic, with PE being zero at equilibrium and KE being maximum, and vice versa.
	
1. **Draw velocity vs time, displacement vs time, and acceleration vs time graphs for \( x(t) = A \sin(\omega t + \theta) \).**
   - **Velocity (v)**: \( v(t) = \frac{dx}{dt} = A\omega \cos(\omega t + \theta) \)
   - **Acceleration (a)**: \( a(t) = \frac{d^2x}{dt^2} = -A\omega^2 \sin(\omega t + \theta) \)
   - The graphs will show sinusoidal variations for each, with velocity leading displacement by \( \pi/2 \) and acceleration leading velocity by \( \pi/2 \).

### Damped Harmonic Motion

1. **What is damped harmonic motion?**
   - Damped harmonic motion occurs when an oscillating system experiences a force that opposes the motion, typically proportional to the velocity, causing the amplitude of the oscillations to decrease over time.

2. **Write the differential equation of damped harmonic motion and explain the significance of each term in the equation.**
   - The differential equation is:
     \[ m\frac{d^2x}{dt^2} + c\frac{dx}{dt} + kx = 0 \]
     where:
     - \( m \) is the mass,
     - \( c \) is the damping coefficient,
     - \( k \) is the stiffness.

3. **Give the conditions for overdamped, critically damped, and underdamped motions.**
   - **Overdamped**: \( c^2 > 4mk \)
   - **Critically damped**: \( c^2 = 4mk \)
   - **Underdamped**: \( c^2 < 4mk \)

4. **Write the time-displacement relationship in each case.**
   - **Underdamped**: \( x(t) = A e^{-\beta t} \cos(\omega_d t + \phi) \)
     - where \( \beta = \frac{c}{2m} \) and \( \omega_d = \sqrt{\omega_0^2 - \beta^2} \)
   - **Critically damped**: \( x(t) = (A + Bt) e^{-\beta t} \)
   - **Overdamped**: \( x(t) = A_1 e^{r_1 t} + A_2 e^{r_2 t} \)
     - where \( r_1 \) and \( r_2 \) are the roots of the characteristic equation.

5. **Draw the displacement-time graph in each case.**
   - **Underdamped**: Oscillatory motion with gradually decreasing amplitude.
   - **Critically damped**: Returns to equilibrium without oscillating, fastest return.
   - **Overdamped**: Returns to equilibrium without oscillating, slower return compared to critically damped.

6. **Define relaxation time, quality factor.**
   - **Relaxation Time**: The time taken for the amplitude of the damped oscillations to reduce to \( 1/e \) of its initial value.
   - **Quality Factor (Q)**: A measure of the damping of the system, defined as \( Q = \frac{m\omega_0}{c} \).

7. **Find the relation between relaxation time and the damping constant. Discuss the significance of the relation.**
   - The relaxation time \( \tau \) is inversely proportional to the damping constant \( \beta \), \( \tau = \frac{1}{\beta} \). A smaller relaxation time indicates higher damping and quicker dissipation of energy.

These explanations cover the key concepts you need to know for your exam. If you need further details or specific derivations, feel free to ask!