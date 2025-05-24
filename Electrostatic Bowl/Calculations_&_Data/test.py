import numpy as np
import matplotlib.pyplot as plt
import time  # import time module

# Start timer
start_time = time.time()

# Load the hemisphere points
coordinates = np.loadtxt('csv/hemesphere.csv', delimiter=',')

# Create a figure and 3D axes
##Plotting the datapoints
fig = plt.figure(dpi = 100)
ax = plt.axes(projection = "3d")
ax.plot3D(coordinates[:, 0], coordinates[:, 1], coordinates[:, 2], ls = " ", marker = ".", mfc = 'red', ms = 5)
plt.grid()
plt.tight_layout()
ax.set_aspect("equal")
plt.show()


# End timer
end_time = time.time()
print(f"Execution time: {end_time - start_time:.4f} seconds")
