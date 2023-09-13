# Ask the user the length of the side of an equilateral triangle. Calculate its area and perimeter.

from math import sqrt
A = int(input('Choose the triangle side length?: '))
Obw = 3 * A
print('Obw of triangle is:', Obw)
P = A ** 2 * sqrt(3) / 4
print('Triangle area is:', P)
