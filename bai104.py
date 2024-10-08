def input_number(str):
    flag = False 
    while not flag: 
        try:
            number = int(input(f"Enter {str}: "))
            if number >= 0: 
                flag=True 
            else:
                print("Enter the positive number!!!")
        except ValueError:
            print("Please enter again !!! Invalid value")
    return number
x = input_number("x")
n = input_number("n")

def calculate(x, n):
    s = 0 
    for i in range(1, n+1): 
        tu = x**i 
        mau = 1 
        for j in range(1, i+1): 
            mau = mau*j 
        s = s + (tu/mau)
    return s 
print("s({0}, {1}) = {2}".format(x,n,calculate(x,n)))
