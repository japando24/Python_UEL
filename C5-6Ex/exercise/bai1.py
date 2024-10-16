def print_first_triangle(n):
    for i in range(n):
        for j in range(i + 1):
            if j % 8 in (1, 2, 3, 4, 5) and (j != i and i != n - 1):
                print("  ", end="")
            else:
                print("* ", end="")
        print()


def print_first_square(n):
    for i in range(n):
        for j in range(n):
            print("* ", end="")
        print()


def print_second_square(n):
    for i in range(n):
        for j in range(n):
            if j % 4 in (1, 2) and (i != 0 and i != 3):
                print("  ", end="")
            else:
                print("* ", end="")
        print()


def print_second_triangle(n):
    for i in range(n):
        for j in range(i + 1):
            print("* ", end="")
        print()


def print_third_triangle(n):
    for i in range(n):
        for j in range(i + 1):
            if j == 0 or j == i or i == n - 1:
                print("* ", end="")
            else:
                print("  ", end="")
        print()


def print_fourth_triangle(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("* ", end="")
        print()


def print_five_triangle(n):
    for i in range(n, 0, -1):
        for j in range(i):
            if i == n or j == 0 or j == i - 1:
                print("* ", end="")
            else:
                print("  ", end="")
        print()
