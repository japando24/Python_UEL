def input_number(str):
    flag = False 
    while not flag: 
        try:
            number = int(input(f"Enter {str}: "))
            if number >= 0: 
                flag=True 
            else:
                print("Enter the positive numbe!!!")
        except ValueError:
            print("Please enter again !!! Invalid value")
    return number
n = input_number("number")
while True: 
    count = 0 
    for i in range(1, n+1): 
        if n%i == 0: 
            count += 1 
    if count==2: 
        print(n, "is prime number")
    else: 
        print(n, "is not prime number")
    answer = input("Do you want to continue ? (Y/y or N/n)")
    if answer is "n" or answer is "N": 
        break 
print("BYE!")