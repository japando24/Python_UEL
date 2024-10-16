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
if n == 1:
    print("Sum 1-n: ", n)
else:
    i = 2
    s = 1
    while i < n:
        s += i
        i += 1
    print("Sum 1-n: ", s + n)
