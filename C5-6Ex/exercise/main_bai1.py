from bai1 import (
    print_first_square,
    print_first_triangle,
    print_five_triangle,
    print_fourth_triangle,
    print_second_square,
    print_second_triangle,
    print_third_triangle,
)


def input_number(str):
    flag = False
    while not flag:
        try:
            number = int(input(f"Enter {str} :"))
            if number > 1:
                flag = True
            else:
                print("You need enter the positive number")
        except ValueError:
            print("Invalid value !!!")
    return number


print("------------------Program draw square and triangle-------------------")
print("1. Draw first geometry")
print("2. Draw second geometry")
print("3. Draw third geometry")
print("4. Draw fourth geometry")
print("5. Draw fifth geometry")
print("6. Draw sixth geometry")
print("7. Draw sixth geometry")
print("8. Exit")
print("---------------------------------------------------------------------")

while True:
    choice = int(input("Enter your choice: "))

    match (choice):
        case 1:
            h = input_number(
                "height which you want to draw with this geometry "
            )
            print_first_triangle(h)
        case 2:
            h = input_number(
                "height which you want to draw with this geometry "
            )
            print_first_square(h)
        case 3:
            h = input_number(
                "height which you want to draw with this geometry "
            )
            print_second_square(h)
        case 4:
            h = input_number(
                "height which you want to draw with this geometry "
            )
            print_second_triangle(h)
        case 5:
            h = input_number(
                "height which you want to draw with this geometry "
            )
            print_third_triangle(h)
        case 6:
            h = input_number(
                "height which you want to draw with this geometry "
            )
            print_fourth_triangle(h)
        case 7:
            h = input_number(
                "height which you want to draw with this geometry "
            )
            print_five_triangle(h)
        case 8:
            print("Do you want to continue ? (Y/y or N/n)")
            answer = input("Enter your answer: ")
            if answer == "Y" or answer == "y":
                break
        case _:
            print("You must enter choice in 1 - 8")
