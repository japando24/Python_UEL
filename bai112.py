def input_number(str):
    flag = False 
    while not flag: 
        try:
            number = float(input(f"Enter {str}: "))
            if number >= 0 and number <= 100: 
                flag=True 
            else:
                print("Enter the positive number and it is smaller than or equal 100 !!!")
        except ValueError:
            print("Please enter again !!! Invalid value")
    return number
rate_physical_exam = input_number("rate people which have physical examination (%)")
rate_unphysical_exam = 100 - rate_physical_exam
rate_exam_unpatients = input_number("rate people which have physical examination and don't have patient: ")
rate_exam_patients = 100 - rate_exam_unpatients
rate_unexam_unpatients = input_number("rate people which don't have physical examination and don't have patient: ")
rate_unexam_patients = 100 - rate_unexam_unpatients 
Result = rate_physical_exam*rate_exam_unpatients/10000+ rate_unphysical_exam*rate_unexam_unpatients/10000
print("Result : ", Result)
