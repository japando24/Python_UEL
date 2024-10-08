def input_number(str):
    flag = False 
    while not flag: 
        try:
            number = int(input(f"Enter {str}: "))
            if number > 0: 
                flag=True 
            else:
                print("Enter the positive number!!!")
        except ValueError:
            print("Please enter again !!! Invalid value")
    return number
n = input_number("n")
def GCDs(n):
    list_gcd = []
    for i in range(1,n): 
        if n % i == 0 : 
            list_gcd.append(i)
    return list_gcd 
def isPerfectOrAbundantNumber(n):
    list_gcd = GCDs(n)
    s = 0 
    for i in list_gcd: 
        s += i 
    if s == n: 
        print(n, "is a perfect number")
    elif s > n: 
        print(n, "is abundant number")
    else: 
        print(n, "is not a perfect number, is not also abundant number")
isPerfectOrAbundantNumber(n)