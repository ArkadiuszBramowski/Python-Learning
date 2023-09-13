# Receive from the user any two points (x1,y1,x2,y2) that form a line segment. Find its center
# Enter the area and center of the circle whose diameter this segment is.
# Consider the area and perimeter of the rectangle whose diagonal is this segment

from math import sqrt
from math import pi
x1 = int(input('Value x1: '))
x2 = int(input('Value x2: '))
y1 = int(input('Value y1: '))
y2 = int(input('Value y2: '))
A = x1, x2
B = y1, y2
C = x2, y1
AB = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f'Straight lane AB is {AB}')
r = AB / 2
x3 = (x1+x2) / 2
y3 = (y1+y2) / 2
print(f'Center of the straight line is {x3},{y3}')
Po = pi * r ** 2
print(f'Field of the circle is {Po}')
Length_rectangle1 = sqrt((x1-x2) ** 2 + (y2-y2) ** 2)
Length_rectangle2 = sqrt((x1-x1) ** 2 + (y1-y2) ** 2)
print(f'Field of rectangle is {Length_rectangle1 * Length_rectangle2}')
print(f'Circuit of the rectangle is {Length_rectangle1 * 2 + Length_rectangle2 * 2}')
