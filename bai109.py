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
buy_price = input_number("buy price")
another_cost = input_number("another costs")
original_price = buy_price + another_cost

year = input_number_int("year")
def annual_depreciation_rate(a,b):
    return a/b
def monthly_depreciation_rate(a):
    return a/12 
def final_period_depreciation(original_price, year, i):
    accumulated_debt = annual_depreciation_rate(original_price, year)*i
    return original_price - accumulated_debt
for i in range(1, year+1): 
    print("+ The period depreciation in ", i, "year", final_period_depreciation(original_price, year, i))
