import numpy as np
import matplotlib.pyplot as plt
import Electric_Potential_and_Field_fn as myfns
import time

##Define the grid
x_grid = np.linspace(-2, 2, 200)
z_grid = np.linspace(-2, 2, 200)
X0, Z0 = np.meshgrid(x_grid, z_grid)

##Initialize the field components
Ex = np.zeros_like(X0)
Ez = np.zeros_like(Z0)

##Initialize potential
phi = np.zeros_like(X0)

##total charge
Q = 1

print("The code is running ...")

##Measuring runtime while running
start_time = time.process_time()

##Potential calculation
for i in range(len(x_grid)):
    for j in range(len(z_grid)):
        x0 = X0[i, j]
        z0 = Z0[i, j]
        y0 = 0                                                                                             ##Calculations on xz-plane
        phi[i,j] = myfns.potential(x0, 0, z0, Q, 8.854e-12)

end_time = time.process_time()

time_taken = end_time - start_time
print(f"Time taken to run is: {time_taken:0.3f}")                                                          ##Printing Runtime


##Compute field
Ez, Ex = np.gradient(-phi)

##____________Potential Plot: Heatmap with colourbar_____________
plt.figure(figsize=(8, 6), dpi = 100)
contour = plt.contourf(X0, Z0, phi, levels=50, cmap='plasma')
plt.streamplot(X0, Z0, Ex, Ez, color='k', linewidth=0.7, density=1.5)

##Plot hemisphere arc
theta_arc = np.linspace(0, np.pi, 200)
x_arc = np.cos(theta_arc)
z_arc = -np.sin(theta_arc)
plt.plot(x_arc, z_arc, color='red', linewidth=3, label = "Shell")

plt.title(f'Potential & Electric Field Lines for total charge = {Q} C')
plt.xlabel('x axis (m)')
plt.ylabel('z axis (m)')
plt.colorbar(contour, label='Potential (V)')
plt.tight_layout()
plt.axis("equal")
plt.savefig("images/potential_field_no_point_charge.png")
plt.show()
