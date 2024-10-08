def input_number(str):
    flag = False 
    while not flag: 
        try:
            number = float(input(f"Enter {str}: "))
            if number > 0: 
                flag = True 
            else:
                print("You must enter the positive float")
        except ValueError:
            print("Invalid value !!!")
    return number 
revenue = input_number("revenue")
cost = input_number("cost")
def ROI(revenue, cost):
    return (revenue - cost)/cost 
def suggestion_investment(roi):
    match roi:
        case x if x > 0.75:
            return "should invest"
        case _:
            return "shouldn't invest"
roi = ROI(revenue, cost)
print("Rate ROI = ", roi)
print("===> ",suggestion_investment(roi))