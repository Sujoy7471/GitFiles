import numpy as np
import matplotlib.pyplot as plt

##Reading the file and saving data in the array
coordinates = np.array(np.loadtxt('csv/hemesphere.csv', delimiter = ','))


##___________Numerical soln____________
##Electric field function
def electric_field(x, y, z, Q = 1, epsilon = 1):
    """ 
    Here in this function we calculate the electric field at any point (x, y, z) numerically.
    """
    charge_per_point = Q / len(coordinates[:,0])
    K = charge_per_point/(4*np.pi*epsilon)
    Ex = K * np.sum( (x - coordinates[:,0]) / ((x - coordinates[:,0])**2 + (y - coordinates[:,1])**2 + (z - coordinates[:,2])**2 )**1.5 + 1e-8 )
    Ey = K * np.sum( (y - coordinates[:,1]) / ((x - coordinates[:,0])**2 + (y - coordinates[:,1])**2 + (z - coordinates[:,2])**2 )**1.5 + 1e-8 )
    Ez = K * np.sum( (z - coordinates[:,2]) / ((x - coordinates[:,0])**2 + (y - coordinates[:,1])**2 + (z - coordinates[:,2])**2 )**1.5 + 1e-8 )

    # For points in y-z plane, cancel any x-component
    if np.abs(x) < 1e-9:
        Ex = 0.0

    # For points in x-z plane, cancel any x-component
    if np.abs(y) < 1e-9:
        Ey = 0.0

    return Ex, Ey, Ez

##Electric potential function
def potential(x, y, z, Q = 1, epsilon = 1):
    """ 
    Here in this function we calculate the electric potential at any point (x, y, z) numerically.
    """
    charge_per_point = Q / len(coordinates[:,0])
    K = charge_per_point/(4*np.pi*epsilon)
    val = np.sum( 1/((x - coordinates[:,0])**2 + (y - coordinates[:,1])**2 + (z - coordinates[:,2])**2 )**0.5 )
    return K*val


##___________Analytical soln____________
##Electric field function
def anal_Ez(z, epsilon, Q = 1):
    if z >= -1:
        val = (1 - 1/np.sqrt(1 + z**2))/(z**2) * (Q / (2*epsilon * 2 * np.pi))
        return val
    elif z < -1:
        val = (-1 - 1/np.sqrt(1 + z**2))/(z**2) * (Q / (2*epsilon * 2 * np.pi))
        return val

##Electric potential function
def anal_potential_z(z, epsilon, Q = 1):
    if z >= -1:
        val = -(Q / (2*epsilon * 2 * np.pi)) * ( np.sqrt(z**2 + 1)/z - 1 - 1/z)
        return val
    elif z < -1:
        val = -(Q / (2*epsilon * 2 * np.pi)) * ( np.sqrt(z**2 + 1)/z + 1 + 1/z)
        return val
