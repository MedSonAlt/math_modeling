import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10, 0.01)

def diff_func(z, t):
    y, omega = z

    dx_dy = omega
    domega_dt = -4*omega-5*y
    return dx_dy, domega_dt

y0 = 4
omega0 = -1

z0 = y0, omega0

sol = odeint(diff_func, z0, t)
plt.plot(t, sol[:, 1], 'b', label='')

plt.legend()
plt.savefig("lab_4.png")