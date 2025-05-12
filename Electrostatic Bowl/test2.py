import numpy as np
import matplotlib.pyplot as plt
import time
import Particle_trajectory_function as ptf

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

def simulate_trajectory(pos, vel, N=70, q=63, Q=1, m=1, g=1, epsilon=1, h=0.1):
    st_time = time.time()

    x, y, z, vx, vy, vz, energy = ptf.particle_motion(
        pos=pos, vel=vel, N=N, q=q, Q=Q, m=m, g=g, epsilon=epsilon, h=h
    )

    end_time = time.time()
    print("Execution time:", end_time - st_time)

    # --- Plot 3D Trajectory with Hemisphere ---
    phi = np.linspace(0, 2 * np.pi, 60)
    theta = np.linspace(0, np.pi / 2, 30)
    phi, theta = np.meshgrid(phi, theta)
    Xh = np.sin(theta) * np.cos(phi)
    Yh = np.sin(theta) * np.sin(phi)
    Zh = -np.cos(theta)

    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, color='red', label='Particle Path')
    ax.plot_surface(Xh, Yh, Zh, color='skyblue', alpha=0.5)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("Trajectory of Particle with Charged Hemisphere")
    ax.legend()
    ax.view_init(elev=30, azim=45)
    set_axes_equal(ax)
    plt.tight_layout()
    plt.show()

    # --- Plot Energy Conservation ---
    plt.figure()
    plt.plot(abs(energy / energy[0] - 1) * 100)
    plt.xlabel('Time step')
    plt.ylabel('Percentage Energy Error')
    plt.title('Energy Conservation')
    plt.grid()
    plt.tight_layout()
    plt.show()

    # --- Plot Velocities ---
    plt.figure()
    plt.plot(vx, label='vx')
    plt.plot(vy, label='vy')
    plt.plot(vz, label='vz')
    plt.xlabel("Time step")
    plt.ylabel("Velocity")
    plt.title("Velocity Components Over Time")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

    return {
        'x': x, 'y': y, 'z': z,
        'vx': vx, 'vy': vy, 'vz': vz,
        'energy': energy,
        'execution_time': end_time - st_time
    }


simulate_trajectory(
    pos=[0, 0, -0.275],
    vel=[0, 0, 0],
    N=300,
    q=63,
    Q=1,
    m=1,
    g=1,
    epsilon=1,
    h=0.1
)
