import numpy as np
import matplotlib.pyplot as plt
import Electric_Potential_and_Field_fn as myfns
import time


time_start = time.time()
z_grid = np.linspace(-2, 2, 300)

Ez = np.zeros_like(z_grid)
phi = np.zeros_like(z_grid)
Ez_anal = np.zeros_like(z_grid)
phi_anal = np.zeros_like(z_grid)

Q = 1
epsilon = 8.854e-12

for i in range(len(z_grid)):
    _, _, Ez[i] = myfns.electric_field(0, 0, z_grid[i], Q, epsilon)
    phi[i] = myfns.potential(0, 0, z_grid[i], Q, epsilon)
    Ez_anal[i] = myfns.anal_Ez(z_grid[i], epsilon, Q)
    phi_anal[i] = myfns.anal_potential_z(z_grid[i], epsilon, Q)
    
time_end = time.time()
print("Time taken for calculation: ", time_end - time_start, " seconds")


plt.figure(dpi = 500, figsize = (15,7.5))
plt.plot(z_grid, Ez, label="Numerical Ez")
plt.plot(z_grid, Ez_anal, linestyle='-', color = 'r', lw = 3,  alpha=0.5, label="Analytical Ez")
plt.xlabel('z-axis')
plt.ylabel('Electric Field (Ez)')
plt.title('Electric Field Comparison along z axis')
plt.legend()
plt.grid(True)
plt.savefig("images/Ez_comparison.png")
plt.show()

plt.figure(dpi = 500, figsize = (15,7.5))
plt.plot(z_grid, phi, label="Numerical Potential")
plt.plot(z_grid, phi_anal, linestyle='-', color = 'r', lw = 3,  alpha=0.5, label="Analytical Potential")
plt.xlabel('z-axis')
plt.ylabel('Potential (Phi)')
plt.title('Potential Comparison along z axis')
plt.legend()
plt.grid(True)
plt.savefig("images/potential_z_comparison.png")
plt.show()
