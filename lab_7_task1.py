import matplotlib.pyplot as plt
import numpy as np
 
 
def cycloid(R=2):
    dd = np.arange(-2*np.pi, 2*np.pi, 0.1)  
 
    y = R * (dd - np.cos(dd) ** 3)
    x = R * (1 - np.sin(dd) ** 3)

    plt.plot(x, y, ls=':', lw=3)
    plt.axis('equal')
    plt.savefig('fig_1.png')
 
if __name__ == '__main__':
    cycloid()