import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.animation as animation

# Load data from file
data = pd.read_csv('output.txt', delimiter=',', header=None)

# Print number of columns
num_cols = data.shape[1]
print(f"Number of columns: {num_cols}")

# Number of particles
num_particles = num_cols // 4

# Initialize storage
x = []
y = []
vx = []
vy = []

# Assign parameters for each particle
for i in range(num_particles):
    x.append(data.iloc[:, 4 * i].values)
    y.append(data.iloc[:, 4 * i + 1].values)
    vx.append(data.iloc[:, 4 * i + 2].values)
    vy.append(data.iloc[:, 4 * i + 3].values)

# Convert lists to NumPy arrays
x = np.array(x)
y = np.array(y)

# Initialize figure
fig, ax = plt.subplots()
ax.set_xlim(-0.05, 1.0+0.05)
ax.set_ylim(-0.05, 1.0+0.05)
ax.set_xlabel("X Position")
ax.set_ylabel("Y Position")


# Scatter plot (initial positions)
scat = ax.scatter(x[:, 0], y[:, 0], color='indigo', s=50)  # Multiple particles

# Update function for animation
def update(frame):
    scat.set_offsets(np.column_stack((x[:, frame], y[:, frame])))  # Update all particles
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(x[0]), interval=25, blit=True, repeat=False)

# Show animation
plt.show()

################################################################
## Analysis if velocity distribution
vxf = np.array(vx)[:, -1]  # Last time step for all particles
vyf = np.array(vy)[:, -1]


vf = np.sqrt(vxf **2 + vyf **2)

##plot the distribution
plt.figure()
plt.hist(vf, bins=25, color='blue', edgecolor='black')
plt.xlabel("Velocity")
plt.ylabel("Count")
plt.title("Final Velocity Distribution")
plt.show()

