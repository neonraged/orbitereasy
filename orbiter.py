# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation


def orbiter_num(a, b):
    # Функция для получения точек орбиты
    t = np.arange(0, 2 * np.pi, 2 * np.pi / 100)
    x = [n*a for n in np.cos(t)]
    y = [m*b for m in np.sin(t)]
    return x, y


def focal_points(a, b):
    # Функция для расчета точек фокуса
    f = [int((a ** 2 - b ** 2) ** 0.5)]
    return f


def exs(a, b):
    # Функция для расчета эксцентриситета
    e = int((1 - (a ** 2)/(b ** 2)) ** 0.5)
    return e


def move_obj(n, x, y, z, point):
    # Функция для обновления положения точки
    point.set_data(np.array([x[n], y[n]]))
    point.set_3d_properties(z, 'z')
    return point


fig = plt.figure()
ax = p3.Axes3D(fig)

a_1 = int(input())  # RX
b_1 = int(input())  # RY
z = 0
x_1, y_1 = orbiter_num(a_1, b_1)

a_2 = int(input())  # RX2
b_2 = int(input())  # RY2
z = 0
x_2, y_2 = orbiter_num(a_2, b_2)

# рисуем орбиту и обьект

obj, = ax.plot([x_1[0]], [y_1[0]], [z], 'o', label='Object')
focal, = ax.plot(focal_points(a_1, b_1), [0], [z], 'o', label='Focal point (Earth)')
orbiter, = ax.plot(x_1, y_1, z, label='Orbiter', ls='dashed', color='#A5BF3F')
obj2, = ax.plot([x_2[0]], [y_2[0]], [z], 'o', label='Object 2')
orbiter2 = ax.plot(x_2, y_2, z, label='Orbiter', ls='dashed', color='#A5BF3F')
ax.legend()
ax.set_xlim([-40, 40])
ax.set_ylim([-40, 40])
ax.set_zlim([-10, 10])

# создаем функцию для апдейта позиции движущегося тела

ani = animation.FuncAnimation(fig, move_obj, 100, fargs=(x_1, y_1, z, obj))
ani2 = animation.FuncAnimation(fig, move_obj, 100, fargs=(x_2, y_2, z, obj2))

plt.show()