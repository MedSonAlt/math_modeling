import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01)

def diff_func(z, x):
    y, omega = z

    dx_dy = omega
    domega_dx = np.sin(x) + np.cos(x)
    return dx_dy, domega_dx

y0 = 3
omega0 = 0

z0 = y0, omega0

sol = odeint(diff_func, z0, x)
plt.plot(x, sol[:, 1], 'b', label='')

plt.legend()
plt.savefig("lab_3.png")