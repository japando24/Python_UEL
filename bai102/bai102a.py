n = 4 
for i in range(n): 
    for j in range(n):
        if (j == 1 or j == 2) and (i!= 0 and i!=3):
            print("  ", end="")
        else: 
            print("* ", end="")
    print()