import matplotlib.pyplot as plt
import numpy as np
 
def elipse_plotter():
    a = 5
    b = 2
    x = np.arange(-3, 2, 0.1)
    y = np.arange(-1, 2, 0.1)
 
    X, Y = np.meshgrid(x, y)
 
    elips = x**2/a**2 + y**2/b**2 == 1
 
    plt.contour(X, Y, elips, levels=[0])

    plt.savefig("fig_task3.png")

if __name__ == "__main__":
    elipse_plotter()