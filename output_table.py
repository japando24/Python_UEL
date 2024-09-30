from tabulate import tabulate

data = [["Name", "Age"], ["Nguyen Bao Huy", 19], ["Nguyen Ha Thu Lan", 15]]
print(tabulate(data, headers="firstrow"))
