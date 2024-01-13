import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
	
def circle_move(radius=10):
    
    x = np.arange(-2*radius, 2*radius, 0.1)
    y = np.arange(-2*radius, 2*radius, 0.1)
 
    X, Y = np.meshgrid(x, y)
 
    fxy = X**2 + Y**2 - radius**2
 
    plt.contour(X, Y, fxy, levels=[0])
    plt.axis("equal")

    plt.savefig("fig_4.png")

def animate(i):
    ball.set_data(circle_move(R=0.5, vx0=0.01, vy0=0.01, time=i))

if __name__ == "__main__":
    circle_move()


