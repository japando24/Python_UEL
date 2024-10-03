height = 5
p = 1 
c = 1
prime = [1,3,5,7,11]
for i in range(5,0,-1):
    for k in range(height-1, i-1, -1):
        print(" ", end="")
    p = 1 
    print(p," ", end=" ")
    while c < (i+1)//2: 
        p = prime[i-c] 
        print(p," ", end="")
        c += 1 
    while c > 1:
        p = prime[i-c]
        print(p, " ", end="") 
        c -= 1 
    print("\n") 