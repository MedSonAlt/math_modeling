import matplotlib.pyplot as plt
import numpy as np
 
def elipse_plotter():
    a = 0.5
    b = 0.2
    x = np.linspace(-1, 1, 50)
    y = np.linspace(-1, 1, 50)
    X, Y = np.meshgrid(x, y)
    elips = (X**2)/(a**2) + (Y**2)/(b**2) - 1
    plt.contour(X, Y, elips, levels=[0])
    plt.axis("equal")
    plt.savefig("fig_task3.png")
    

if __name__ == "__main__":
    elipse_plotter()