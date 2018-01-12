import math
r = float(input())

area = math.pi * r**2
length = 2 * r * math.pi

print("{:.6f} {:.6f}".format(area, length))