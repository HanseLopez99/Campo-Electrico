import numpy as np
from scipy.integrate import quad
k = 8.988e9  # Coulomb Constant

def electric_field_ring(r, x):
    """
    Calculate electric field due to a ring charge at an observation point.
    
    """
    micro_coulomb = 1.0e-6
    
    ring_charge_density = micro_coulomb / (2 * np.pi * r)
    
    def integrand(dl, r, x):
        return k * ring_charge_density * x / (r**2 + x**2)**(1.5)
    
    E, _ = quad(integrand, 0, 2 * np.pi * r, args=(r, x))
    E_formatted = "{:.3f}".format(E)
    return E_formatted

def electric_field_disk(r, x):
    """
    Compute electric field produced by a charged disk at a specific x position.
    """
    micro_coulomb = 1.0e-6
    
    disk_charge_density = micro_coulomb / (np.pi * r**2)
    
    def integrand(r, x):
        dA = 2 * np.pi * r
        dQ = disk_charge_density * dA
        return k * dQ * x / (r**2 + x**2)**(3/2)
    
    E, _ = quad(integrand, 0, r, args=(x,))
    E_formatted = "{:.3f}".format(E)
    return E_formatted

def electric_field_line(l, x):
    """
    Evaluate electric field due to a line charge at a specific x-coordinate.
    """
    micro_coulomb = 1.0e-6
    
    line_charge_density = micro_coulomb / l
    
    def integrand(y, x):
        dL = 1
        dQ = line_charge_density * dL
        return k * dQ * x / (x**2 + y**2)**(3/2)
    
    E, _ = quad(integrand, -l/2, l/2, args=(x,))
    E_formatted = "{:.3f}".format(E)
    return E_formatted

anillo = electric_field_ring(1, 1)
print(anillo)

disco = electric_field_disk(1, 1)
print(disco)

vara = electric_field_line(1, 1)
print(vara)
