# import the constant pi from the math module
from math import pi
# cylinder height
h = float(input('h = '))
# cylinder base radius
r = float(input('r = '))
# A cylinder has two bases
# the area of each base is Pi * R * R
circles = 2 * (pi * r ** 2)
# the area of the side of the surface of a cylinder is 2 * pi * R  * H.
side = 2 * pi * r * h
# total surface area
area = circles + side
print('A = '+ str(round(area, 2)))
