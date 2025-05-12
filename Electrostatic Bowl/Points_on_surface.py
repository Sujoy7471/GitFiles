import numpy as np
import matplotlib.pyplot as plt
import time

def generate_points(N):
    """
    This function generates N random points on the surface of a hemisphere of radius 1 that lies between x = [-1, 1], y = [-1, 1], z = [-1, 0].
    Algorithm: 
        It generate N random values of phi in the range [0, 2*pi]
        Now to get uniform distribution, it generate cdf of sin(theta) [0<= theta <= pi/2], i.e, cos(theta) = z in uniform distribution between [0,1] range.
        Then run this N times in the loop to get N points.
    """
    coordinates = []
    for i in range(N):
        z = np.random.uniform(0, 1)
        phi = np.random.uniform(0, 2*np.pi)
        coordinates.append([np.sqrt(1 - z**2)*np.cos(phi), np.sqrt(1 - z**2)*np.sin(phi), -z])
    return coordinates

##Recording time
start_time = time.process_time()

## Generating the points
coordinates = np.array(generate_points(500000))

end_time = time.process_time()
elapsed_time = end_time - start_time

print(f"Time taken = {elapsed_time} seconds")

##Saving the datapoints
np.savetxt("csv/hemesphere.csv", coordinates, delimiter=",", comments="")
print("Datapoints are saved in the file 'hemesphere.csv' ")

##Plotting the datapoints
fig = plt.figure(dpi = 100)
ax = plt.axes(projection = "3d")
ax.plot3D(coordinates[:, 0], coordinates[:, 1], coordinates[:, 2], ls = " ", marker = ".", mfc = 'red', ms = 5)
plt.grid()
plt.tight_layout()
ax.set_aspect("equal")
plt.show()
