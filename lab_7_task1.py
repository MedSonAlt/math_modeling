import matplotlib.pyplot as plt
import numpy as np
 
 
def cycloid(R=2):
    t = np.arange(-2*np.pi, 2*np.pi, 0.1)  
 
    x = R * (t - (np.sin(t))**3)
    y = R * (1 - (np.cos(t))**3)

    plt.plot(x, y, ls=':', lw=3)
    plt.axis('equal')
    plt.savefig('fig_1_Cycloid.png')
    plt.close()
 

def astroid(R = 2):
    t = np.arange(-2*np.pi, 2*np.pi, 0.1)  
 
    x = R * np.cos(t)**3
    y = R * np.sin(t)**3

    plt.plot(x, y, ls=':', lw=3)
    plt.axis('equal')
    plt.savefig('fig_1_astroida.png')
    plt.close()


if __name__ == '__main__':
    cycloid()
    astroid()