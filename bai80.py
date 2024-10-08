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
def BMI(height, weight):
    return weight/(height*height)
def classification(bmi): 
    match bmi:
        case x if x < 18.5:
            return "Gầy"
        case x if x <= 24.9:
            return "Bình thường"
        case x if x <= 29.9:
            return "Hơi béo"
        case x if x <= 34.9:
            return "Béo phì cấp độ 1"
        case x if x <= 39.9:
            return "Béo phì cấp độ 2"
        case _:
            return "Béo phì cấp độ 3"
    # if bmi < 8.5: 
    #     return "Gầy"
    # elif bmi <= 24.9:
    #     return "Bình thường"
    # elif bmi <= 29.9:
    #     return "Hơi béo"
    # elif bmi <= 34.9: 
    #     return "Béo phì Cấp độ 1"
    # elif bmi <= 39.9:
    #     return "Béo phì cấp độ 2"
    # else: 
    #     return "Béo phì cấp độ 3"
def risk_disease(bmi): 
    match bmi: 
        case x if x < 18.5: 
            return "Thấp"
        case x if x < 24.9: 
            return "Trung Bình"
        case x if x < 29.9: 
            return "Cao"
        case x if x < 34.9:
            return "Cao"
        case x if x < 39.9:
            return "Rất cao"
        case _: 
            return "Nguy hiểm"
height = input_number("height (m): ")
weight = input_number("weight (kg): ")
bmi = BMI(height, weight)
print("Your BMI: ", bmi)
print("Your classification: ", classification(bmi))
print("Risk of disease: ", risk_disease(bmi))