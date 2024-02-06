import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10, 0.001)

def monetki(n,t):
    dn_dt = -k*n*t
    return dn_dt
n_0 = 1000
k = 0.05

n_t = odeint(monetki, n_0, t)
plt.plot(t, n_t[:,0], label='Размножение ')
plt.savefig('инвестиции.png')