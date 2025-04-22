import numpy as np
import matplotlib.pyplot as plt
import time
##Grid setup
N = 100  ##Grid size (NxN)

##Convergence parameter
tolerance = 1e-5
max_iterations = 10000


def jacobi(phi):
    phi_new = phi.copy()
    for iteration in range(max_iterations):
        phi_old = phi_new.copy()
        for i in range(1, N-1):
            for j in range(1, N-1):
                phi_new[i,j] = 0.25*(phi_old[i+1,j] + phi_old[i-1,j] + phi_old[i,j+1] + phi_old[i,j-1])

        diff = np.linalg.norm(phi_new - phi_old) ##Try alternatives
        if diff < tolerance:
            break   ##Try alternatives
    return phi_new, iteration

def gauss_seidal(phi):
    phi_new = phi.copy()
    for iteration in range(max_iterations):
        phi_old = phi_new.copy()
        for i in range(1, N-1):
            for j in range(1, N-1):
                phi_new[i,j] = 0.25*(phi_new[i+1,j] + phi_new[i-1,j] + phi_new[i,j+1] + phi_new[i,j-1])
        diff = np.linalg.norm(phi_new - phi_old) ##Try alternatives
        if diff < tolerance:
            break   ##Try alternatives
    return phi_new, iteration


def sor(phi, omega= 1.5):
    phi_new = phi.copy()
    for iteration in range(max_iterations):
        phi_old = phi_new.copy()
        for i in range(1, N-1):
            for j in range(1, N-1):
                phi_new[i,j] = (1 - omega)*phi_old[i,j] + (omega/4)*(phi_new[i+1,j] + phi_new[i-1,j] + phi_new[i,j+1] + phi_new[i,j-1])
        diff = np.linalg.norm(phi_new - phi_old) ##Try alternatives
        if diff < tolerance:
            break   ##Try alternatives
    return phi_new, iteration

def run_algorithm(algorithm, *args):
    phi_init = np.zeros((N, N))
    phi_init[:, N-1] = 100
    start_time = time.time()
    result, steps = algorithm(phi_init, *args)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return result, steps, elapsed_time


jacobi_result, j_steps, j_time = run_algorithm(jacobi)
gauss_seidal_result, gs_steps, gs_time = run_algorithm(gauss_seidal)
sor_result, sor_steps, sor_time = run_algorithm(sor)



plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.imshow(jacobi_result, cmap='hot', interpolation='nearest')
plt.title(f'Jacobi\nSteps: {j_steps}\nTime: {j_time:.4f}s')
plt.colorbar()
plt.subplot(1, 3, 2)
plt.imshow(gauss_seidal_result, cmap='hot', interpolation='nearest')
plt.title(f'Gauss-Seidal\nSteps: {gs_steps}\nTime: {gs_time:.4f}s')
plt.colorbar()
plt.subplot(1, 3, 3)
plt.imshow(sor_result, cmap='hot', interpolation='nearest')
plt.title(f'SOR\nSteps: {sor_steps}\nTime: {sor_time:.4f}s')
plt.colorbar()
plt.tight_layout()
plt.savefig('convergence_methods.png')
plt.show()