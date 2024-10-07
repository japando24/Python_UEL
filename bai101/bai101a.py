n=4 
for i in range(1, 2*n):
    if i < n:
        for j in range(3):
            print("  ", end="")
        for k in range(i): 
            print("* ", end="")
        for m in range(n-i):
            print("  ", end="")
        print()
    elif i == n:
        for j in range(2*n-1):
            print("* ", end="")
        print()
    else: 
        for j in range(2*n-i):
            print("* ", end="")
        for k in range(i): 
            print("  ", end="")
        print()
