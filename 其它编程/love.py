# -*- coding: utf-8 -*-
# @Time    : 2018/5/20 17:20
# @Author  : di.yu
# @Email   : yudi_mars@126.com
# @File    : love.py
# @Software: Sublime Text 3

import matplotlib.pyplot as plt  
from matplotlib import animation  
import numpy as np  
import math  
  
figure = plt.figure()  
axes = plt.axes(xlim=(-2, 2), ylim=(-2, 2)) 
axes.set_axis_off()
line1, = axes.plot([], [], color='pink', linewidth=8, label='1')  
line2, = axes.plot([], [], color='pink', linewidth=8, label='2')  
  
  
def init():  
    line1.set_data([], [])  
    line2.set_data([], [])  
    return line1, line2  
  
  
def animate(i):  
    print('(づ￣ 3￣)づ')  
    t = np.linspace(0, i/math.pi, 100)  
    x = np.sin(t) 
    y = np.cos(t) + np.power(x, 2.0/3)  
    line1.set_data(x, y)  
    line2.set_data(-x, y)  
    return line1, line2  
  
  
ani = animation.FuncAnimation(figure, animate, init_func=init, frames=14, interval=100)
plt.title("Best wish for you~")
plt.show() 