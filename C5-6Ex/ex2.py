def input_number(str):
    flag = False
    while not flag:
        try:
            number = int(input(f"Enter {str} :"))
            if number > 0:
                flag = True
            else:
                print("You need enter the positive number")
        except ValueError:
            print("Invalid value !!!")
    return number


n = input_number("number")
s = 0
print("The first way: ")
for i in range(0, n + 1, 2):
    s += i
print("Result: ", s)
print("The second way: ")
i = 0
s = 0
while i <= n:
    s += i
    i += 2
print("Result: ", s)
