def average(list_result):
    sum = 0
    for i in list_result:
        sum += i
    return sum/len(list_result)
try:
    toan = float(input("Enter math: "))
    ly = float(input("Enter physics: "))
    hoa = float(input("Enter chemistry: "))
    list_result = list([toan, ly, hoa])
    dtb = average(list_result)
    print("Average: ", dtb)
except:
    print("Error !!!")