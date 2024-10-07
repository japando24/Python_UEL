import math 
def input_coefficient():
    flag = False 
    while not flag: 
        try:
            my_int = float(input("Enter number: "))
            flag = True
        except ValueError:
            print("Please enter again !!! Invalid value")
    return my_int
a = input_coefficient()
b = input_coefficient()
c = input_coefficient() 
if a == 0:
    if b == 0 and c == 0: 
        print("Equation has infinite solutions")
    elif b== 0 and c != 0: 
        print("Equation has no solutions")
    else: 
        x = -c/b 
        print("Equation has one solution : ",x) 
else: 
    delta = b**2 - 4*c*a 
    if delta < 0: 
        print("Equation has no solutions")
    elif delta == 0: 
        x = -b/(2*a)
        print("Equation has one solution : ",x)
    else: 
        x1 = (-b - math.sqrt(delta))/(2*a)
        x2 = (-b + math.sqrt(delta))/(2*a)
        print("x1 = ", x1)
        print("x2 = ", x2)

