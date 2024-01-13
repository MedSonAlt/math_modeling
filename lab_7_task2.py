import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
	
def circle_move(R, angle_vel, time):
    alpha = angle_vel * np.pi / 180 * time
    x = R * np.cos(alpha)
    y = R * np.sin(alpha)
    return x, y
