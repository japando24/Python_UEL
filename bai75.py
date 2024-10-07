def input_number():
    flag = False 
    while not flag: 
        try:
            my_int = int(input("Enter number: "))
            if my_int < 100: 
                flag = True
            else: 
                print("You need to enter the number which has 2 digits or 1 digit")
        except ValueError:
            print("Please enter again !!! Invalid value")
    return my_int
one_digit_dictionary = {
    "0":"zero", 
    "1":"one", 
    "2":"two",
    "3":"three", 
    "4":"four",
    "5":"five", 
    "6":"six", 
    "7":"seven", 
    "8":"eight",
    "9":"nine"
};
under_twenty_dictionary = {
    "10": "ten", 
    "11": "eleven", 
    "12": "twelve", 
    "13": "thirteen", 
    "14": "fourteen", 
    "15": "fifteen",
    "16": "sixteen", 
    "17": "seventeen", 
    "18": "eighteen", 
    "19": "nineteen", 
}
two_digit_dictionary = {
    "2":"twenty",
    "3":"thirty", 
    "4":"forty", 
    "5":"fifty", 
    "6":"sixty",
    "7":"seventy",
    "8":"eighty",
    "9":"ninety", 
}
num = input_number()
str_len=len(str(num))
str_num=str(num)
if str_len == 1: 
    print(one_digit_dictionary[str_num])
else: 
    if 10 <= num and num <= 19: 
        print(under_twenty_dictionary[str_num])
    elif num != 10 and num % 10 == 0: 
        print(two_digit_dictionary[str_num[0]])
    else: 
        print(two_digit_dictionary[str_num[0]],"-",one_digit_dictionary[str_num[1]])
