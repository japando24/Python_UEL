flag = True
def hour(t):
    a = int((t/3600)%24)
    hour = a if a < 12 else a%12
    flag = False
    return hour
unit = "AM" if flag else "PM"
def minute(t):
    return int((t%3600)/60)
def second(t):
    return int((t%3600)%60)
try:
    t = int(input("Enter any second: "))
    print(hour(t),":", minute(t),":",second(t),f"{unit}")
except:
    print("Error!!!")