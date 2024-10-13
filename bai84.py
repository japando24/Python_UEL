def input():
    flag = False 
    while not flag: 
        try:
            my_int = int(input("Enter number: "))
            if my_int > 0: 
                flag = True 
            else: 
                print("You must be enter the positive number !!!")
        except ValueError:
            print("Please enter again !!! Invalid value")
    return my_int
n = input() 
i = 2 
s = 1 
if n == 1: 
    print("Sum of 1-n: ", s)
else: 
    while i <= n: 
        s += s + i 
        i += 1 
    print("Sum of 1-n: ", s)
    