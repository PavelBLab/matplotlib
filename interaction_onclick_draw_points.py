import numpy as np
import matplotlib.pyplot as plt

points = []

def onclick(event):
    global points
    points.append([event.xdata, event.ydata])

    ax.plot(event.xdata, event.ydata,'o')
    plt.draw()


fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_xlim((0, 10))
ax.set_ylim((0, 10))

plt.gcf().canvas.mpl_connect('button_press_event', onclick)

plt.show()
print(points)