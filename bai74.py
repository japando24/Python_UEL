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
int_dictionary = {
    "0": "không", 
    "1": "một", 
    "2": "hai", 
    "3": "ba", 
    "4": "bốn",
    "5": "năm", 
    "6": "sáu", 
    "7": "bảy", 
    "8": "tám", 
    "9": "chín"
}
num = input_number()
num_length = len(str(num))
str_num = str(num)
if num_length == 1: 
    print(int_dictionary[str_num])
else:
    if num == 10: 
        print("mười")
    elif num != 10 and num % 10 == 0: 
        print(int_dictionary[str_num[0]]," mươi")
    else: 
        if str_num[0] == "1": 
            if str_num[1] == 5: 
                print("mười lăm")
            else: 
                print("mười", int_dictionary[str_num[1]])

        elif str_num[1] == "5": 
            print(int_dictionary[str_num[0]]," mươi lăm")
        elif str_num[1] == "4": 
            print(int_dictionary[str_num[0]]," mươi tư")
        elif str_num[1] == "1":
            print(int_dictionary[str_num[0]], " mươi mốt")
        else:
            print(int_dictionary[str_num[0]], " mươi ",int_dictionary[str_num[1]])
        # match(str_num[1]):
        #     case "1": 
        #         print(int_dictionary[str_num[0]], " mươi mốt")
        #     case "4": 
        #         print(int_dictionary[str_num[0]]," mươi tư")
        #     case "5":
        #         print(int_dictionary[str_num[0]]," mươi lăm")
        # if str_num[0] == "1": 
        #         print("mười", int_dictionary[str_num[1]])
        # else: 
        #     print(int_dictionary[str_num[0]], " mươi ",int_dictionary[str_num[1]])