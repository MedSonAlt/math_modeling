import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 20, 0.001)

def monetki(v,t):
    dn_dt = g - y*v**2
    return dn_dt

g = 10
y = 0.2
v_0 = 0

n_t = odeint(monetki, v_0, t)
plt.plot(t, n_t[:,0], label='хех ')
plt.savefig('изм скорости со временем.png')