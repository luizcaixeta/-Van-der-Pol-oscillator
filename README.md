The Van der Pol oscillator is a nonlinear second-order differential equation often used to model self-sustaining oscillations. It's particularly famous for its use in electrical circuits, though its applications extend to biology, physics, and engineering, among other fields.

The equation for the Van der Pol oscillator is:

$$
\frac{d^2x}{dt^2} - \mu(1 - x^2) \frac{dx}{dt} + x = 0
$$

Where:
- x represents the system's state (e.g., position, voltage, etc.),
- μ is a nonlinearity parameter that controls the strength of the damping,
- The term \(μ(1 - x^2) \frac{dx}{dt}\) introduces the nonlinearity, causing the damping to change depending on the amplitude of the oscillations.

When \(μ = 0\), the system behaves like a simple harmonic oscillator, exhibiting regular sinusoidal motion. As \(\mu\) increases, the oscillator's behavior becomes more complex, with characteristics like relaxation oscillations, where the system spends more time in one phase of the oscillation and quickly jumps to the next.

The Van der Pol oscillator is especially interesting because it demonstrates limit cycle behavior. Regardless of the initial conditions, the system will tend toward a periodic oscillation with a fixed amplitude and frequency (for sufficiently large \(\mu\)), a phenomenon known as a limit cycle.

This system can be used to model biological rhythms (like heartbeat), electrical circuits (such as relaxation oscillators), and even certain aspects of neural firing patterns.

In this case: μ = 2



![a](https://github.com/user-attachments/assets/919a78ef-18a1-4387-b05e-be8443145e3c)
