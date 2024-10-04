height = 5
p = 1 
c = 1
prime = [1,7,7,1]
for i in range(5,0,-1):
    for k in range(height-1, i-1, -1):
        print(" ", end=" ")
    if i == 5: 
        for m in range(len(prime)): 
            if m == 1: 
                print(prime[m],"",11," ", end="")
            else: 
                print(prime[m]," ", end="")
        print("\n")
    else:
        for j in range(i): 
            if j == 0 or j == i-1:
                print("1 ", end=" ")
            else: 
                if j == 2: 
                    print(5, " ", end="")
                else: 
                    print(prime[j] - prime[j-1] -1," ",end="") 
                prime=[1,5,5,1]
        print("\n")