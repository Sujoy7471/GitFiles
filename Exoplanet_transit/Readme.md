# Exoplanet Transit Light Curve Modeling  
**Planetary system:** HD 209458

This project is a curiosity-driven attempt to understand how exoplanet transit light curves arise directly from orbital geometry and stellar physics, rather than relying on pre-built analytical transit models. Using real photometric data of the well-studied hot-Jupiter system **HD 209458**, I built a numerical transit model from scratch and used it to extract basic system parameters.

The emphasis of this work is on **physical intuition and transparency**, not on producing a publication-ready model.

---

## Motivation

Transit light curves are often introduced through analytical formulae or black-box fitting tools. I wanted to understand the process at a more fundamental level:

- How does a planet’s motion across a stellar disk translate into a dip in observed flux?
- How do inclination and planet size affect the transit depth and shape?
- How does stellar limb darkening modify the curvature of the light curve?

To explore these questions, I implemented a **Monte Carlo transit model** that directly computes the fractional loss of stellar light during a transit.

---

## Data

Real photometric time-series data of **HD 209458** were used.

Data preparation steps:
- Conversion from magnitude to relative flux
- Selection of time windows containing transit events
- Binning and thinning of the light curve to reduce noise
- Identification of individual transit minima

---

## Method Overview

### 1. Transit Timing and Orbital Period

- Individual transit minima were identified by fitting symmetric polynomials to thinned transit data.
- The time difference between successive minima was used to estimate the orbital period.

---

### 2. Orbital Geometry

- A circular orbit was assumed.
- The planetary orbit was projected onto the plane of the sky with a variable inclination.
- Only configurations where the planet lies in front of the star (line-of-sight condition) produce a transit.

---

### 3. Stellar Disk Model (Monte Carlo)

- The stellar disk was modeled using randomly generated surface points uniformly distributed over a circular disk.
- Each surface element was assigned a brightness weight using a **quadratic limb-darkening law**:
  
  \[
  I(\mu) = 1 - u(1 - \mu) - v(1 - \mu)^2
  \]

This provides a physically motivated brightness distribution across the stellar surface.

---

### 4. Transit Simulation

- At each time step, stellar surface elements blocked by the planetary disk were identified using a geometric masking condition.
- The blocked luminosity was computed and normalized by the total stellar luminosity.
- The resulting fractional flux defines the simulated transit light curve.

This approach avoids analytical transit formulae and instead performs a direct numerical integration of the occulted stellar surface.

---

### 5. Parameter Estimation

A grid-based search was performed over:
- orbital inclination
- planet-to-star radius ratio

The best-fit parameters were selected by minimizing the squared difference between the simulated and observed light curves.

---

## Results

From the analysis of **HD 209458**, the following parameters were obtained:

- **Orbital period:**  
  **3.52519901 ± 0.00039853 days**

- **Orbital radius:**  
  **(6.78 ± 0.10) × 10⁹ m**  
  **≈ 8.12 ± 0.12 stellar radii**

- **Orbital inclination (assuming circular orbit):**  
  **85.817°**

- **Planet-to-star radius ratio:**  
  **Rp / Rs = 0.13028**

- **Planetary radius:**  
  **≈ 1.52 Jupiter radii**  
  (**≈ 17.1 Earth radii**)

The simulated light curve reproduces the observed transit depth and overall shape reasonably well, given the simplicity of the model and the stochastic nature of Monte Carlo sampling.

---

## Notes and Limitations

- The model is computationally expensive due to Monte Carlo sampling.
- A circular orbit is assumed.
- Limb-darkening coefficients are fixed (taken from literature) and not fitted.
- Error estimates are approximate and intended for exploratory purposes.

Despite these simplifications, the model captures the essential physics underlying transit light curves.

---

## Purpose of the Project

This was a short, exploratory project carried out to:
- build intuition about transit geometry
- understand the role of limb darkening
- learn how physical parameters imprint themselves on observed light curves

The project is intended as a **self-learning exercise**, not as a finalized scientific analysis.
