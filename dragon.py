# Heighway’s Dragon Curve
# Inspired by code written by Amartya Ranjan Saikia

import math

from display import *
from draw import *

s = new_screen()

iteration = 10
length = 5 
color = [0, 255, 0]

r, l = 'r', 'l'
xa, ya, xb, yb = XRES/2, YRES/2, XRES/2, YRES/2
dx, dy = 0, 0
heading = 0

iter = 0
previous = r 
current = previous

while iter < 12: 
    current = previous + r 
    previous = previous[::-1]  
    for cur in range(len(previous)):  
        if previous[cur] == r:  
            previous = previous[:cur]+ l + previous[cur + 1:]
        else:
            previous = previous[:cur] + r + previous[cur + 1:] 
    current = current + previous  
  
    previous = current  
    iter += 1

for i in range(len(current)):
    if current[i] == r:
        heading -= math.pi / 2
    else:
        heading += math.pi / 2

    dx = length * math.sin(heading)
    dy = length * math.cos(heading)

    color[RED] = int(xa % 255)

    draw_line(xa, ya, xa + dx, ya + dy, s, color)

    xa += dx
    ya += dy 

    draw_line(xb, yb, xb - dx, yb - dy, s, color)

    xb -= dx
    yb -= dy

display(s)
save_extension(s, 'dragon.png')