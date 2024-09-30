import math
def perimeter(r):
    pa = 2 * math.pi * r
    return pa
def square(r):
    square = math.pi*r**2
    return square
try:
    r = float(input("Enter radius: "))
    print("Perimeter: ", perimeter(r))
    print("Square: ", square(r))
except:
    print("Error")
