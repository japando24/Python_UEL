def input_number(str):
    flag = False 
    while not flag: 
        try:
            number = float(input(f"Enter {str}: "))
            if number > 0: 
                flag=True 
            else:
                print("Enter the positive number!!!")
        except ValueError:
            print("Please enter again !!! Invalid value")
    return number
def input_number_int(str):
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
r = input_number("interest rate of 3 month (%)")
n = input_number_int("years of deposit ")
deposit_money = input_number(" how much money to deposit ")
num_term = n * 4
interest_rate_term = 0 
result = deposit_money
for i in range(num_term): 
    interest_rate_term = result*r/100*3 
    result = result + interest_rate_term
print("Money which you can get after: ", result) 
        