n = 4 
for i in range(2*n-1): 
    if i < n-1:
        for j in range(n-1):
            print("  ", end="")
        for k in range(n - i):
            print("* ", end="")
        for m in range(i):
            print("  ",end="")
        print() 
    elif i == n-1:
        for j in range(n-1):
            print("  ", end="")
        print("* ")
    else:
        for j in range(2*n-2-i):
            print("  ",end="")
        for m in range(i+2-n): 
            print("* ",end="")
        print()  