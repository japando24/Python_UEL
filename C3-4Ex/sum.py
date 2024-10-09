def input_number(str):
    flag = False
    while not flag:
        try:
            num = int(input(str))
            if 0 < num:
                flag = True
            else:
                print(
                    "You need to enter the positive number !!! Please try again"
                )
        except ValueError:
            print("Invalid value!!!")
    return num


n = input_number(str)
# sum = (n+1)*n/2
# print(sum)
result = 1
if n == 1:
    print(n)
else:
    for i in range(2, n + 1):
        result += i
    print(result)
