def tinh(N): 
    s = 1 
    i = 1 
    while i <= N: 
        if i%3 == 0: 
            s *= i 
        i += 1 
    return s 
N= 8 
for i in range(1,10): 
    if (i > N): 
        print("===="+str(tinh(i)))