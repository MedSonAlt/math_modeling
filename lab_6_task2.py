import matplotlib.pyplot as plt
import numpy as np
def giperbola_plotter():
    k = 2
    x = np.arange(10, 10, 0.01)
    y = k/x 
    plt.plot(x, y, label='my + giperbola')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.title('giperbola')
    plt.legend()

    
    plt.savefig('fig_task2.png')

if __name__ == '__main__':
    giperbola_plotter()