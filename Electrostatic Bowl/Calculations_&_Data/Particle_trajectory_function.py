import numpy as np
import Electric_Potential_and_Field_fn as myfns

def particle_motion(pos, vel, q, Q=1, m=1, g=1, N = 1000, h=0.01, epsilon=1):
    ''' 
    pos = initial position (3-element list or array)
    vel = initial velocity (3-element list or array)
    q = charge of the particle
    Q = total charge on hemisphere
    m = mass of the particle
    g = gravitational acceleration
    N = number of time steps
    h = time step
    epsilon = permittivity
    '''

    # Initialize arrays to store the results
    x = np.zeros(N+1)
    y = np.zeros(N+1)
    z = np.zeros(N+1)
    vx = np.zeros(N+1)
    vy = np.zeros(N+1)
    vz = np.zeros(N+1)
    energy = np.zeros(N+1)

    # Set initial conditions
    x[0], y[0], z[0] = pos
    vx[0], vy[0], vz[0] = vel

    def acceleration(x, y, z):
        Ex, Ey, Ez = myfns.electric_field(x, y, z, Q, epsilon)
        ax = (q * Ex) / m
        ay = (q * Ey) / m
        az = (q * Ez - m * g) / m
        return np.array([ax, ay, az])

    for i in range(N):
        r = np.array([x[i], y[i], z[i]])
        v = np.array([vx[i], vy[i], vz[i]])

        # RK4 coefficients for velocity and position
        a1 = acceleration(*r)
        k1_v = h * a1
        k1_r = h * v

        a2 = acceleration(*(r + 0.5 * k1_r))
        k2_v = h * a2
        k2_r = h * (v + 0.5 * k1_v)

        a3 = acceleration(*(r + 0.5 * k2_r))
        k3_v = h * a3
        k3_r = h * (v + 0.5 * k2_v)

        a4 = acceleration(*(r + k3_r))
        k4_v = h * a4
        k4_r = h * (v + k3_v)

        # Update velocity and position
        v_next = v + (k1_v + 2*k2_v + 2*k3_v + k4_v) / 6
        r_next = r + (k1_r + 2*k2_r + 2*k3_r + k4_r) / 6

        # Save next step
        x[i+1], y[i+1], z[i+1] = r_next
        vx[i+1], vy[i+1], vz[i+1] = v_next

        # Energy at step i
        potential_energy = myfns.potential(x[i], y[i], z[i], Q, epsilon) * q
        kinetic_energy = 0.5 * m * (vx[i]**2 + vy[i]**2 + vz[i]**2)
        gravitational_energy = m * g * z[i]
        energy[i] = potential_energy + kinetic_energy + gravitational_energy

    # Final energy point
    potential_energy = myfns.potential(x[N], y[N], z[N], Q, epsilon) * q
    kinetic_energy = 0.5 * m * (vx[N]**2 + vy[N]**2 + vz[N]**2)
    gravitational_energy = m * g * z[N]
    energy[N] = potential_energy + kinetic_energy + gravitational_energy

    return np.array(x), np.array(y), np.array(z), np.array(vx), np.array(vy), np.array(vz), np.array(energy)
