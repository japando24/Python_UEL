def input_month():
    flag = False 
    while not flag: 
        try:
            month = float(input("Enter month: "))

            if 1 <= month and month <= 12: 
                flag = True 
            else: 
                print("Please enter month in 1-12 !!!")
        except ValueError:
            print("Please enter again !!! Invalid value")
    return month
month = input_month() 
match(month): 
    case 1|2|3: 
        print("In the first quarter")
    case 4|5|6: 
        print("In the second quarter")
    case 7|8|9:
        print("In the third quarter")
    case 10|11|12:
        print("In the fourth quarter")