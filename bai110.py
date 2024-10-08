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
num_patients = input_number_int("number of patients")
num_cured = input_number_int("number of people cured")
def factorial(n):
    if n == 1 or n == 0: 
        return 1 
    return n*factorial(n-1)
def calculate(num_patients, num_cured):
    return ((num_patients - num_cured)*factorial(num_patients-1))/(factorial(num_patients))
print("Result: ", calculate(num_patients, num_cured))