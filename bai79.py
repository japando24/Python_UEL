import math 
def input_number():
    flag = False 
    while not flag: 
        try:
            length = float(input("Enter length of triangle: "))
            if length > 0: 
                flag=True 
            else:
                print("Enter the positive length for triangle !!!")
        except ValueError:
            print("Please enter again !!! Invalid value")
    return length
def p(a,b,c):
    return (a+b+c)/2 
def square(a,b,c):
    pv = p(a,b,c) 
    return math.sqrt(pv*(pv-a)*(pv-b)*(pv-c))
def valid_triangle(a,b,c):
    if a+b > c and b+c > a and c+a > b: 
        return True 
    else: 
        return False 
a = input_number()
b = input_number() 
c = input_number() 
if valid_triangle(a,b,c):
    print("Square triangle : ", square(a,b,c))
else: 
    print("Please start again, you need to enter the length of triangle in valid value!!!!")