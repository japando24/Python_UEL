n = 4 
for i in range(2*n-1): 
    if i < n-1:  
        for j in range(i+1):
            if i == 2 and j == 1: 
                print("  ", end="")
            else: 
                print("* ", end="") 

        for k in range(2*n-1-i,0,-1):
            print(" ", end="")
        print("\n")
    elif i == n-1: 
        for j in range(2*n-1): 
            print("* ", end="")
        print("\n")
    else: 
        for k in range(i): 
            print("  ", end="")
        for j in range(2*n-i-1, 0, -1): 
            if i == 4 and j == 2: 
                print("  ", end="")
            else: 
                print("* ", end="")
        print("\n")
