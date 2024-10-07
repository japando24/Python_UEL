def input_year():
    flag = False 
    while not flag: 
        try:
            year = int(input("Enter year: "))
            if (year > 0):
                flag = True 
            else: 
                print("Enter position year!!!") 
        except ValueError: 
            print("Invalid value !!! Please enter again")
    return year
year = input_year() 
if (year%4 == 0 and year%100 != 0) or year%400 == 0:
    print(year,"is leap year")
else:
    print(year,"is not leap year")
 