import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 47, 0.001)

def microchel(n,t):
    dn_dt = k*n
    return dn_dt
n_0 = 5
k = 0.05

n_t = odeint(microchel, n_0, t)

plt.plot(t, n_t[:,0], label='Размножение ')
plt.xlabel('Период размножения, минуты')
plt.ylabel('Функция распада')
plt.title('Радиоактивный распад')
plt.legend()
plt.savefig('бактерии.png')