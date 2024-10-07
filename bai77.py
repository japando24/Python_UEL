def input_number():
    flag = False 
    while not flag: 
        try:
            my_int = float(input("Enter number: "))
            flag = True 
        except ValueError:
            print("Please enter again !!! Invalid value")
    return my_int
def input_operator():
    flag = False 
    while not flag: 
        try:
            operator = input("Enter operator: ")
            if operator in ("+", "-", "/", "*"):
                flag = True 
            else:
                print("Please enter operator in ["+", "-", "/", "*"]")
        except ValueError:
            print("Please enter again !!! Invalida value") 
    return operator
a = input_number()
b = input_number() 
operator = input_operator() 
match(operator):
    case "+":
        print(f"{a} {operator} {b} = {a+b}")
    case "-":
        print(f"{a} {operator} {b} = {a-b}")
    case "*":
        print(f"{a} {operator} {b} = {a*b}")
    case "/": 
        print(f"{a} {operator} {b} = {a/b}")