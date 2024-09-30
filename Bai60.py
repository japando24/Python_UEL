def input_x():
    flag = False
    while not flag:
        try:
            x = int(input("Enter x:"))
            str_check = str(x)
            if len(str_check) == 3:
                flag=True
            else:
                print("You need to enter the number which has 3 digits")
        except ValueError:
            print("Invalid number !!! Try again")
    return int(x)
def reverse(x):
    result = ""
    while x != 0:
        digit = x%10
        x //= 10
        result = result + str(digit)
    return int(result)
x = input_x()
result = reverse(x)
print(result)