h = 3


def print_geometry(h):
    for i in range(2 * h - 1):
        for j in range(2 * h - 1):
            if (
                i == 0
                or i == 2 * h - 2
                or j == i
                or j == 2
                or (j == 3 and i == 1)
                or (j == 1 and i == 3)
            ):
                print("* ", end="")
            else:
                print("  ", end="")
        print()


print_geometry(h)
