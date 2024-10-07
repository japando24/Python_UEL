import math 
def input_number():
    flag = False 
    while not flag: 
        try:
            number = int(input("Enter number: "))
            if number > 0: 
                flag=True 
            else:
                print("Enter the positive number !!!")
        except ValueError:
            print("Please enter again !!! Invalid value")
    return number 
n = input_number() 
s = math.sqrt(2)
for i in range (1,n): 
    s = math.sqrt(2 + s)
print("Result : ", s)