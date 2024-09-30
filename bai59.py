import math
def calculate_log(a,x):
    return math.log(x)/math.log(a)
def input_x():
    flag = False
    while not flag:
        try:
            x = float(input("Enter x:"))
            if x > 0:
                flag = True
            else:
                print("You need to enter x has positive value !!!")
        except ValueError:
            print("Invalid number !!! Try again")
    return x
def input_a():
    flag=False
    while not flag:
        try:
            a=float(input("Enter a: "))
            if a > 0 and a != 1:
                flag = True
            else:
                print("You need to enter a has position value and not equal 1 !!!")
        except ValueError:
            print("Invalid number !!! Try again")
    return a
try:
    x = input_x()
    a = input_a()
    result = calculate_log(a,x)
    print("Result : ", result)
except:
    print("Error !!!")