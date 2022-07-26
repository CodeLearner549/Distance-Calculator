# Distance Calculator
import math

print("Welcome to the Distance Calculator")

x1 = float(input("Enter x1: "))
x2 = float(input("Enter x2: "))
y1 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))


def dist_function(a, b, c, d):
    rise = c - d
    run = b - a
    return math.sqrt(rise ** 2 + run ** 2)


dist = dist_function(x1, x2, y1, y2)
print("Distance between points is " + str(dist) + ".")
