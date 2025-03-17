import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Load data from file
data = pd.read_csv('output_3d.txt', delimiter=',', header=None)

# Print number of columns
num_cols = data.shape[1]
print(f"Number of columns: {num_cols}")

# Number of particles
num_particles = num_cols // 6  # 6 columns per particle (x, y, z, vx, vy, vz)

# Initialize storage
x, y, z = [], [], []
vx, vy, vz = [], [], []

# Assign parameters for each particle
for i in range(num_particles):
    x.append(data.iloc[:, 6 * i].values)
    y.append(data.iloc[:, 6 * i + 1].values)
    z.append(data.iloc[:, 6 * i + 2].values)
    vx.append(data.iloc[:, 6 * i + 3].values)
    vy.append(data.iloc[:, 6 * i + 4].values)
    vz.append(data.iloc[:, 6 * i + 5].values)

# Convert lists to NumPy arrays
x, y, z = np.array(x), np.array(y), np.array(z)

offset = 0

# Initialize figure for 3D animation
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(offset, 1 + offset)
ax.set_ylim(offset, 1 + offset)
ax.set_zlim(offset, 1 + offset)
ax.set_xlabel("X Position")
ax.set_ylabel("Y Position")
ax.set_zlabel("Z Position")

# Scatter plot (initial positions)
scat = ax.scatter(x[:, 0], y[:, 0], z[:, 0], color='brown', s=20)

# Update function for animation
def update(frame):
    scat._offsets3d = (x[:, frame], y[:, frame], z[:, frame])
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(x[0]), interval=10, blit=False, repeat=False)

# Show animation
plt.show()

################################################################
## Analysis of velocity distribution
vxf = np.array(vx)[:, -1]  # Last time step for all particles
vyf = np.array(vy)[:, -1]
vzf = np.array(vz)[:, -1]

vf = np.sqrt(vxf ** 2 + vyf ** 2 + vzf ** 2)  # 3D speed

# Plot the distribution
plt.figure()
plt.hist(vf, bins=10, color='blue', edgecolor='black')
plt.xlabel("Velocity")
plt.ylabel("Count")
plt.title("Final Velocity Distribution in 3D")
plt.show()