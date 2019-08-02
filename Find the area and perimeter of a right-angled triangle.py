import math
AB = input('Length of the first leg: ')
AC = input('Length of the second leg: ')

AB = float(AB)
AC = float(AC)

BC = math.sqrt(AB ** 2 + AC ** 2)

S = (AB * AC) / 2
P = AB + AC + BC

print('Area of the triangle: %.2f' % S)
print('Perimeter of the triangle: %.2f' % P)
