import matplotlib.pyplot as plt
import numpy as np
import grouper


points = [(-1, 3), (2, -4), (1, 0), (3, -2), (-1, 0)]  # Initial list of ordered pairs.
""""
Points is the list of points you want to average, each list item is an ordered pair (x, y).
Replace the empty list in the points variable with a list of tuples, which are ordered pairs.
ex: [(0,1), (2, 3), (4, 5)]
"""

x_points = []  # Empty list of x-points.
y_points = []  # Empty list of y-points.
for x, y in points:  # Appends all points from the list to their respective list of points.
    x_points.append(x)
    y_points.append(y)

fig, ax = plt.subplots(1, 1)

# X, Y AXIS CODE V
# set the x-spine (see below for more info on `set_position`)
ax.spines['left'].set_position('zero')

# turn off the right spine/ticks
ax.spines['right'].set_color('none')
ax.yaxis.tick_left()

# set the y-spine
ax.spines['bottom'].set_position('zero')

# turn off the top spine/ticks
ax.spines['top'].set_color('none')
ax.xaxis.tick_bottom()
# X, Y AXIS CODE ^

plt.scatter(np.asarray(x_points), np.asarray(y_points), c='black')
plt.scatter(*np.asarray(grouper.get_average(points)), c='red')

plt.show()
