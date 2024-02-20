import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-1, 1, 0.01)

def diff_func(f, t):
    x, y = f

    dx_dt = 3 * x - 2 * y + e**(3*t) / (e**t + 1)
    dy_dt = x - e**(3*t)/(e**t + 1)
    return dx_dt, dy_dt

x0 = 5
y0 = -7
e = 2.718
f0 = x0, y0


sol = odeint(diff_func, f0, t)
plt.plot(t, sol[:, 1], 'r', label='')

plt.legend()
plt.savefig("lab_2.png")