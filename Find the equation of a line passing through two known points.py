print("A(x1; y1):")
#\t is like pressing tab before writing the input
x1 = float(input("\tx1 = "))
y1 = float(input("\ty1 = "))
print("B(x2; y2):")
x2 = float(input("\tx2 = "))
y2 = float(input("\ty2 = "))
print("Equation: ")
k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2
print("\ty = %.2f*x + %.2f" % (k, b))
