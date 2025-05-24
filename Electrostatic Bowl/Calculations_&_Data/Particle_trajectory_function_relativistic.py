import numpy as np
import Electric_Potential_and_Field_fn as myfns

def particle_motion(pos, vel, q, Q=1, m0=1, g=1, N = 1000, h=0.01, epsilon=1):
    ''' 
    pos = initial position (3-element list or array)
    vel = initial velocity (3-element list or array)
    q = charge of the particle
    Q = total charge on hemisphere
    m0 = mass of the particle
    g = gravitational acceleration
    N = number of time steps
    h = time step
    epsilon = permittivity
    '''
    ##Speed of light
    c = 3e8
    ##Rest energy
    E0 = m0*c**2

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

    def acceleration(x, y, z, m):
        Ex, Ey, Ez = myfns.electric_field(x, y, z, Q, epsilon)
        ax = (q * Ex)
        ay = (q * Ey)
        az = (q * Ez - m * g)
        return np.array([ax, ay, az])

    for i in range(N):
        r = np.array([x[i], y[i], z[i]])
        v = np.array([vx[i], vy[i], vz[i]])

        ##Calculating the relativistic mass in each point
        v2modi = (v[0]**2 + v[1]**2 + v[2]**2)
        m = m0/np.sqrt( 1 - v2modi/c**2)

        # RK4 coefficients for velocity and position
        a1 = acceleration(*r, m)
        k1_v = h * a1/m
        k1_r = h * v

        a2 = acceleration(*(r + 0.5 * k1_r), m)
        k2_v = h * a2
        k2_r = h * (v + 0.5 * k1_v)

        a3 = acceleration(*(r + 0.5 * k2_r), m)
        k3_v = h * a3
        k3_r = h * (v + 0.5 * k2_v)

        a4 = acceleration(*(r + k3_r), m)
        k4_v = h * a4
        k4_r = h * (v + k3_v)

        # Update velocity and position
        v_next = v + (k1_v + 2*k2_v + 2*k3_v + k4_v) / 6
        r_next = r + (k1_r + 2*k2_r + 2*k3_r + k4_r) / 6

        # Save next step
        x[i+1], y[i+1], z[i+1] = r_next
        vx[i+1], vy[i+1], vz[i+1] = v_next

        # Energy at step i
        gamma = 1 / np.sqrt(1 - v2modi / c**2)
        m = gamma * m0
        potential_energy = myfns.potential(x[i], y[i], z[i], Q, epsilon) * q
        gravitational_energy = m * g * z[i]
        total_mass_energy = gamma * m0 * c**2 + potential_energy + gravitational_energy
        energy[i] = total_mass_energy


    # Final energy point
    v_final2 = vx[N]**2 + vy[N]**2 + vz[N]**2
    gamma = 1 / np.sqrt(1 - v_final2 / c**2)
    m = gamma * m0
    potential_energy = myfns.potential(x[N], y[N], z[N], Q, epsilon) * q
    gravitational_energy = m * g * z[N]
    total_mass_energy = gamma * m0 * c**2 + potential_energy + gravitational_energy
    energy[N] = total_mass_energy

    return np.array(x), np.array(y), np.array(z), np.array(vx), np.array(vy), np.array(vz), np.array(energy)