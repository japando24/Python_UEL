def kiemtra(n):
    S =0 
    if n%2 == 1: 
        S==0
    for i in range(1, n/2 + 1): 
        if (n%i == 0):
            s = s + i 
    if S == n:    
        return 1 
n = int(input("Nhập vào một số n: "))
for i in range(1, n+1): 
    if kiemtra(i) == i: 
        print(i)