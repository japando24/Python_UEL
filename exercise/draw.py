def draw(h): 
    for i in range(2*h - 1): 
        for j in range(2*h-1): 
            # if (j >= i and i + j <= 2*h-2) or (j <= i and i+j >= 2*h-2): 
            if i <= j <= 2*h-2 - i or 2*h - 2 - i <= j <= i or j == 0 or j == 2*h - 2: 
                print("* ", end="")
            else:
                print("  ", end="")
        print()
draw(4) 