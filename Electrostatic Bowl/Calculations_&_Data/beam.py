import numpy as np
import Particle_trajectory_function as ptf
import matplotlib.pyplot as plt
import time

st_time = time.time()


# --- Particle Trajectory Function ---
x1, y1, z1, _, _, _, energy1 = ptf.particle_motion(pos = [0, 5, 2], vel = [0, -1e4, 0], N = 73, q = -1.6e-19, Q = 1e-7, m = 9.1e-31, g = 9.8, epsilon=8.854e-12, h = 1.5e-8)
x2, y2, z2, _, _, _, energy2 = ptf.particle_motion(pos = [0, 5, 2], vel = [0, -1e6, 0], N = 67, q = -1.6e-19, Q = 1e-7, m = 9.1e-31, g = 9.8, epsilon=8.854e-12, h = 1.5e-8)
x3, y3, z3, _, _, _, energy3 = ptf.particle_motion(pos = [0, 5, 2], vel = [0, -2.5e6, 0], N = 58, q = -1.6e-19, Q = 1e-7, m = 9.1e-31, g = 9.8, epsilon=8.854e-12, h = 1.5e-8)
x4, y4, z4, _, _, _, energy4 = ptf.particle_motion(pos = [0, 5, 2], vel = [0, -5e6, 0], N = 49, q = -1.6e-19, Q = 1e-7, m = 9.1e-31, g = 9.8, epsilon=8.854e-12, h = 1.5e-8)
x5, y5, z5, _, _, _, energy5 = ptf.particle_motion(pos = [0, 5, 2], vel = [0, -1e7, 0], N = 40, q = -1.6e-19, Q = 1e-7, m = 9.1e-31, g = 9.8, epsilon=8.854e-12, h = 1.5e-8)
end_time = time.time()

print("Execution time: ", end_time - st_time)

# --- Plotting Part ---
def set_axes_equal(ax):
    '''Set 3D plot axes to equal scale (same length for x, y, z).'''
    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    plot_radius = 0.5 * max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])


# Create hemisphere
phi = np.linspace(0, 2 * np.pi, 60)
theta = np.linspace(0, np.pi / 2, 30)
phi, theta = np.meshgrid(phi, theta)
Xh = np.sin(theta) * np.cos(phi)
Yh = np.sin(theta) * np.sin(phi)
Zh = -np.cos(theta)

# Plot
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x1, y1, z1, color=(1.0, 0.6, 0.6), label='v_y = -1e4 m/s')
ax.plot(x2, y2, z2, color=(1.0, 0.4, 0.4), label='v_y = -1e6 m/s')
ax.plot(x3, y3, z3, color=(1.0, 0.2, 0.2), label='v_y = -2.5e6 m/s')
ax.plot(x4, y4, z4, color=(0.8, 0.0, 0.0), label='v_y = -5e6 m/s')
ax.plot(x5, y5, z5, color=(0.6, 0.0, 0.0), label='v_y = -1e7 m/s')
ax.plot_surface(Xh, Yh, Zh, color='skyblue', alpha=0.5)

# Labels & view
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Trajectory of Particles with Charged Hemisphere")
ax.legend()
ax.view_init(elev=30, azim=45)
set_axes_equal(ax)
plt.tight_layout()
plt.show()


plt.figure()
plt.plot(abs(energy1/energy1[0] -1)*100, label = 'v_y = -1e4 m/s')
plt.plot(abs(energy2/energy2[0] -1)*100, label = 'v_y = -1e6 m/s')
plt.plot(abs(energy3/energy3[0] -1)*100, label = 'v_y = -2.5e6 m/s')
plt.plot(abs(energy4/energy4[0] -1)*100, label = 'v_y = -5e6 m/s')
plt.plot(abs(energy5/energy5[0] -1)*100, label = 'v_y = -1e7 m/s')
plt.xlabel('Time step')
plt.ylabel('Percentage Energy Error')
plt.title('Energy Conservation')
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()

