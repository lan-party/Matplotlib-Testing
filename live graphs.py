import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
import _thread
import numpy as np
import time

style.use('dark_background')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


def f(x):
    r = []
    for x_num in x:
        r += [np.sin(x_num)]
    return r
def f2(x):
    r = []
    for x_num in x:
        r += [np.cos(x_num)]
    return r


def animate(i):
    x = np.arange(1,i,0.1)
    y = f(x)
    y2 = f2(x)
    ax1.clear()
    ax1.plot(x, y)
    ax1.plot(x, y2)
    time.sleep(0.1)

ani = animation.FuncAnimation(fig, animate, interval=100)

ani.save('live graphs.gif', writer='imagemagick', fps=60)




