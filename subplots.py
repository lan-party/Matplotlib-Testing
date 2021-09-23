import matplotlib.pyplot as plt
import random

fig = plt.figure()

def create_plots():
    xs = []
    ys = []
    for i in range(10):
        x = i
        y = random.randrange(10)
        xs.append(x)
        ys.append(y)
    return xs, ys

ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(212)

x,y = create_plots()
ax1.plot(x,y)
x,y = create_plots()
ax2.plot(x,y)

plt.savefig("subplots.png")
