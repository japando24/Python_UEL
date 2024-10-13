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
def input_str(str): 
    flag = False 
    while not flag: 
        try:
            str_info = input(f"Enter {str}: ")
            if len(str_info) > 0: 
                flag = True 
            else:
                print("You must enter the unempty string!!!")
        except ValueError:
            print("Invalid value !!!")
    return str_info
name_customer = input_str("fullname of customer")
group_customer = input_str("group customer (1: postpaid, 2: prepaid)")
num_elec = input_number(" n.o kWh")
dictionary_rank_elec = {
    "1": 1.549, 
    "2": 1.600, 
    "3": 1.858, 
    "4": 2.340, 
    "5": 2.615, 
    "6": 2.701, 
}
def spend_elec(group_customer, num_elec):
    if group_customer == "1": 
        match num_elec: 
            case x if x <=50: 
                return num_elec*dictionary_rank_elec["1"]
            case x if x <=100: 
                return 50*dictionary_rank_elec["1"] + (num_elec-50)*dictionary_rank_elec["2"]
            case x if x <= 200: 
                return 50*dictionary_rank_elec["1"]+50*dictionary_rank_elec["2"] + (num_elec-100)*dictionary_rank_elec["3"]
            case x if x <= 300:
                return 50*dictionary_rank_elec["1"]+50*dictionary_rank_elec["2"] +100*dictionary_rank_elec["3"] + (num_elec-200)*dictionary_rank_elec["4"]
            case x if x <= 400: 
                return 50*dictionary_rank_elec["1"]+50*dictionary_rank_elec["2"] +100*dictionary_rank_elec["3"]+100*dictionary_rank_elec["4"] + (num_elec-300)*dictionary_rank_elec["5"]
            case _: 
                return 50*dictionary_rank_elec["1"]+50*dictionary_rank_elec["2"] +100*dictionary_rank_elec["3"]+100*dictionary_rank_elec["4"]+100*dictionary_rank_elec["5"] + (num_elec-400)*dictionary_rank_elec["6"]
    elif group_customer == "2":
        return num_elec*2.271 
    else:
        print("Invalid value, group_customer must have value 1 or 2")
result = spend_elec(group_customer, num_elec)
print("Result: ",result)