def input_number(str):
    flag = False
    while not flag:
        try:
            num = int(input(str))
            if 0 < num:
                flag = True
            else:
                print("You need to enter the positive number")
        except ValueError:
            print("Invalid value!!!")
    return num


n = input_number("Enter number: ")
# sum = (n+1)*n/2
# print(sum)
result = 1
if n == 1:
    print(result)
else:
    for i in range(2, n + 1):
        result += i
    print(result)
