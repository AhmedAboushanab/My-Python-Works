import math
#the math module contains the power function pow() and the constant pi
r = input("Radius = ")
#the string is converted to a float number
r = float(r)
#the length of the circumference is 2 * pi * R
length_of_the_circumference = 2 * math.pi * r
#the area of the circle is Pi * R * R
area = math.pi * math.pow(r, 2)
#note: in python, you can raise the power using the operator **
#then:
#area = math.pi * r**2
print("length = %.2f" % length_of_the_circumference)
print("Area = %.2f" % area)
