def GCD(a, b):
    while a != b: 
        if a > b: 
            a = a - b 
        else: 
            b = b - a 
    return a 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("GCD: ", GCD(a,b))
print(-16/GCD(a,b))