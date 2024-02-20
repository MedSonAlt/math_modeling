import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10, 0.01)

def diff_func(z, t):
    theta, omega = z

    y_dt = omega
    domega_dt = np.sin(theta) * omega - 3*t*theta-5
    return y_dt, domega_dt

y0 = 0.01
omega0 = 0.05

z0 = y0, omega0

sol = odeint(diff_func, z0, t)
plt.plot(t, sol[:, 1], 'y', label=')')
plt.plot(t, sol[:, 0], 'b', label='')

plt.legend()
plt.savefig("hz_9.png")