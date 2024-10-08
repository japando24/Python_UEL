def input_number_float(str):
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
def input_number_int(str): 
    flag = False 
    while not flag: 
        try:
            num = int(input(f"Enter {str}: "))
            if num > 0: 
                flag = True 
            else:
                print("You must enter the positive number!!!")
        except ValueError:
            print("Invalid value !!!")
    return num
old_elc = input_number_float("old n.o electronic (kWh)")
new_elc = input_number_float("new n.o electronic (kWh)")
num_fam = input_number_int("n.o family which use electric meter")
classification_elc = input_number_int("type of electricity: (1: daily activities, 2: business, 3: manufacturer)")
dict_rank_elec={
    "1": 1484, 
    "2": 1533,
    "3": 1786, 
    "4": 2242, 
    "5": 2503, 
    "6": 2587, 
}
business_unit = 2320 
manufacture_unit = 1518 
def spend_elec(classification_elc, A, B, C):
    match classification_elc:
        case 1: 
            match (B-A):
                case x if x <= 50*C: 
                    return (B-A) * dict_rank_elec["1"]
                case x if x <= 100*C: 
                    return (50*C * dict_rank_elec["1"]) + ((B-A) - 50*C) * dict_rank_elec["2"]
                case x if x <= 200*C: 
                    return (50*C*dict_rank_elec["1"]) + (50*C*dict_rank_elec["2"]) + ((B-A) - 100*C)*dict_rank_elec["3"]
                case x if x <= 300*C: 
                    return (50*C*dict_rank_elec["1"]) + (50*C*dict_rank_elec["2"]) + (100*C*dict_rank_elec["3"]) + ((B-A) - 200*C) * dict_rank_elec["4"]
                case x if x <= 400*C: 
                    return (50*C*dict_rank_elec["1"]) + (50*C*dict_rank_elec["2"]) + (100*C*dict_rank_elec["3"]) + (100*C*dict_rank_elec["4"]) + ((B-A) - 300*C) *dict_rank_elec["5"]
                case _: 
                    return (50*C*dict_rank_elec["1"]) + (50*C*dict_rank_elec["2"]) + (100*C*dict_rank_elec["3"]) + (100*C*dict_rank_elec["4"]) + 100*C*dict_rank_elec["5"] + ((B-A) - 400*C)*dict_rank_elec["6"]
        case 2: 
            return (B-A)*business_unit
        case 3: 
            return (B-A)*manufacture_unit 
        case _:
            print("You must enter the classification in 1-3 !!!")
result = spend_elec(classification_elc, old_elc, new_elc, num_fam)
print("Money of spending for electricity: ", result)

    
        