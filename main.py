import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

r = 0.5
step = 0.03
rotation_speed = 0.01

x = np.arange(-5, 2 * 2 * np.pi, step)
#print("y = ax + b")
#function_a = input("a: ")
#function_b = input("b: ")
#y = float(function_a) * x + float(function_b)

function = input("y = ")


def f(x):
    return eval(function, {'x': x})


y = f(x)

# roznice miedzy punktami
delta_x = np.roll(x, 1) - x
delta_y = np.roll(y, 1) - y

# wspolczynnik kierunkowy
tangent_slope = delta_y / delta_x

cycloid_x_points = []
cycloid_y_points = []

fig, ax = plt.subplots()
ax.set_xlim(-5, max(x))
ax.set_ylim(-5, 5)
function1, = ax.plot(x, y)
function2, = ax.plot(0, 0)
cycloid_center, = ax.plot(0, 0, marker='o')
draw_cycloid, = ax.plot(0, 0)
cycloid_arm, = ax.plot(0, 0)


def frame(i):

    try:
        A = tangent_slope[i]
        v = np.array([A, -1])
        v = r * v / np.sqrt(np.sum(v ** 2))

        alpha = np.arange(0, 2 * np.pi+0.01, 0.66*np.pi)
        alpha = alpha - i*2*np.pi*rotation_speed
        cycloid_x = r * np.cos(alpha) + x[i] - v[0]
        cycloid_y = r * np.sin(alpha) + y[i] - v[1]
        length = (len(cycloid_x)-1)/2
        cycloid_x_points.append(cycloid_x[int(length)])
        cycloid_y_points.append(cycloid_y[int(length)])
        function2.set_data(cycloid_x, cycloid_y)
        cycloid_center.set_data(x[i] - v[0], y[i] - v[1])
        draw_cycloid.set_data(cycloid_x_points, cycloid_y_points)
        cycloid_arm.set_data([x[i] - v[0], cycloid_x[int(length)]], [y[i] - v[1], cycloid_y[int(length)]])

        return function2, cycloid_center, draw_cycloid, cycloid_arm

    except Exception as e:
        print(e)


animation = FuncAnimation(fig, func=frame, frames=len(tangent_slope), interval=1, repeat=False)

plt.show()
