def input_month():
    flag = False 
    while not flag: 
        try:
            month = int(input("Enter month: "))
            if month < 1 or month > 12: 
                print("Please enter month in range 1-12")
            else: 
                flag=True 
        except ValueError:
            print("Invalid Value !!! Please enter again") 
    return month 
def input_year():
    flag = False 
    while not flag: 
        try:
            year = int(input("Enter year: "))
            if year > 0: 
                flag = True 
            else: 
                print("Please enter positive year !!!")
        except ValueError:
            print("Invalid Value !!! Please enter again") 
    return year 
month = input_month()
year = input_year()
month_dictionary = {
    1: "January", 
    2: "February", 
    3: "March", 
    4: "April", 
    5: "May", 
    6: "June", 
    7: "July", 
    8: "August", 
    9: "September",
    10: "October", 
    11: "November", 
    12: "December"
}
def print_result(month, year ): 
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            print(month_dictionary[month]," has ",31," days.")
        case 4 | 6 | 9 | 11:
            print(month_dictionary[month], " has ",30, " days.")
        case 2: 
            if (year % 4 == 0 and year % 100 == 0) or year % 400 == 0: 
                print(month_dictionary[month], " has ", 29, " days.")
            else:
                print(month_dictionary[month], " has ", 28, " days.")
print_result(month, year)
        
