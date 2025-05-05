import numpy as np
from pythtb import *
import matplotlib.pyplot as plt
from multiprocessing import Pool

# Constants
e = 1  # elementary charge (Coulombs)
hbar = 1  # reduced Planck constant (J·s)
Nk = 50  # k-mesh size in each direction (for 50x50x50 grid)
eta = 0.0001  # broadening parameter
fermi_energy = 6.87  # Fermi energy in eV (update this with your material's Fermi energy)

# Load the tight-binding model (replace with your model files)
pgda = w90("PdGa_Ham2", "wannier90")  # Replace with your model filenames
my_model = pgda.model(min_hopping_norm=0.01)

# Generate a k-point mesh (in the 3D Brillouin Zone)
k_mesh = np.linspace(0, 1, Nk, endpoint=False)
kpoints = np.array(np.meshgrid(k_mesh, k_mesh, k_mesh)).T.reshape(-1, 3)

# Initialize total orbital Hall conductivity
total_ohc = 0
volume_element = (2 * np.pi)**3 / len(kpoints)  # Normalized BZ volume per k-point

# Function to calculate the velocity operator at a k-point
def calculate_v(k_vec, my_model, dk=0.01):
    """
    Calculate the velocity operator at a k-point using finite difference approximation.
    
    Parameters:
    - k_vec: k-point at which to calculate the velocity operator (3x1 numpy array)
    - my_model: Tight-binding model object containing the Hamiltonian
    - dk: Small perturbation value for finite difference (default: 0.01)
    
    Returns:
    - velocity: A 3x3 numpy array containing the components of the velocity operator (vx, vy, vz)
    """
    # Generate the Hamiltonian at the k-point k_vec and perturbed k-points
    H = my_model._gen_ham(k_vec)  # Original Hamiltonian at k-point
    Hx = my_model._gen_ham([k_vec[0] + dk, k_vec[1], k_vec[2]])  # Perturbed in x-direction
    Hy = my_model._gen_ham([k_vec[0], k_vec[1] + dk, k_vec[2]])  # Perturbed in y-direction
    Hz = my_model._gen_ham([k_vec[0], k_vec[1], k_vec[2] + dk])  # Perturbed in z-direction

    # Calculate the finite difference for each component of the velocity
    vx = (Hx - H) / dk
    vy = (Hy - H) / dk
    vz = (Hz - H) / dk

    # Return the velocity operator as a 3x3 matrix
    return np.array([vx, vy, vz])

# Function to solve for Omega and calculate the orbital Hall conductivity components
def solve_and_calculate_Omega_xyz(k_vec, my_model, eta=0.0001):
    """
    This function calculates the orbital Hall conductivity component for a given k-point.
    
    Parameters:
    - k_vec: k-point at which to calculate the Omega values (3x1 numpy array)
    - my_model: Tight-binding model object
    - eta: Small parameter for avoiding singularities (default: 0.0001)
    
    Returns:
    - evals: Eigenvalues of the Hamiltonian at k_vec
    - Omega_xyz: Orbital Hall conductivity components at k_vec
    """
    v = calculate_v(k_vec, my_model)  # Get velocity operator at k-point
    eig_values, eig_vectors = my_model.solve_one(k_vec, eig_vectors=True)  # Solve the model at k-point
    
    # Initialize the orbital angular momentum components
    Lz = np.zeros(eig_values.shape[0])
    
    # Calculate the orbital angular momentum component Lz
    for n in range(eig_values.shape[0]):
        temp = 0
        for m in range(eig_values.shape[0]):
            if m == n:
                continue
            temp += (eig_vectors[n].conjugate().dot(v[0]).dot(eig_vectors[m]) * eig_vectors[m].conjugate().dot(v[1]).dot(eig_vectors[n])) / (eig_values[n] - eig_values[m] + complex(0, eta))
            temp -= (eig_vectors[n].conjugate().dot(v[1]).dot(eig_vectors[m]) * eig_vectors[m].conjugate().dot(v[0]).dot(eig_vectors[n])) / (eig_values[n] - eig_values[m] + complex(0, eta))
        Lz[n] = np.imag(temp)
    
    # Calculate the Omega^z_xy (orbital Hall conductivity component)
    Omega_xyz = np.zeros(eig_values.shape[0])
    for n in range(eig_values.shape[0]):
        temp = 0
        for m in range(eig_values.shape[0]):
            if m == n:
                continue
            temp -= (Lz[m] + Lz[n]) * (eig_vectors[n].conjugate().dot(v[0]).dot(eig_vectors[m]) * eig_vectors[m].conjugate().dot(v[1]).dot(eig_vectors[n])) / (eig_values[n] - eig_values[m] + complex(0, eta))**2
        Omega_xyz[n] = np.imag(temp / 2)

    return eig_values, Omega_xyz

# Function to process a chunk of k-points
def process_kpoints_chunk(kpoints_chunk):
    total_ohc_chunk = 0
    for k_vec in kpoints_chunk:
        evals, Omega = solve_and_calculate_Omega_xyz(k_vec, my_model, eta=eta)
        # Sum Omega for occupied bands (below the Fermi energy)
        for n in range(len(evals)):
            if evals[n] < fermi_energy:
                total_ohc_chunk += Omega[n]
    return total_ohc_chunk

# Split the k-points into 4 chunks
num_chunks = 4
chunks = np.array_split(kpoints, num_chunks)

# Parallelize the calculation across 4 cores
with Pool(processes=num_chunks) as pool:
    results = pool.map(process_kpoints_chunk, chunks)

# Combine the results from all chunks
total_ohc = sum(results)

# Final value of OHC (unit: ℏ/e·Å)
ohc = total_ohc * volume_element / (2 * np.pi)**3  # Already in ℏ=1 units

# Save the result to a file
output_file = "orbital_hall_conductivity.txt"
with open(output_file, "w") as file:
    file.write(f"Orbital Hall Conductivity (OHC) in ℏ/e·Å units: {ohc}\n")

print(f"Result saved to {output_file}")
