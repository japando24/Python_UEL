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
print(a,"x + ",b,"=0")
if a == 0: 
    if b == 0: 
        print("Equation has infinite solutions")
    else:
        print("Equation has not solution")
else:
    print(f"Equation has one solution: {(-b)/a}")
