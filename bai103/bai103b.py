def generate_pascals_triangle(n): 
    triangle = [[1]]
    for i in range(1, n): 
        row=[1]
        for j in range(1, i): 
            row.append(triangle[i-1][j-1] + triangle[i-1][j]+1)
        row.append(1)
        triangle.append(row)
    return triangle
def print_triangle(h): 
    triangle = generate_pascals_triangle(5)[::-1]
    for i in range(1, 2*h):
        if i <= h: 
            j = 0       
            c = i // 2        
            try: 
                while j < i: 
                    if (i%2 == 0 and j%2 == 0) or (i%2 == 1 and j%2 == 1):
                        print("   ", end="")
                        if j == 0: 
                            c -= 1
                        j += 1 
                    else: 
                        print(triangle[j][c], end=" ")
                        j += 1
                        c -= 1
            except IndexError: 
                print("  ", end="")
            for k in range(h-i): 
                print("  ", end="")
            print("")
        else: 
            j=0
            c=i//2
            try: 

                while j < (2*h - i): 
                    if (i%2 == 0 and j%2 == 0) or (i%2 == 1 and j%2 == 1):
                        print("   ", end="")
                        if j == 0: 
                            c -= 1
                        j+=1
                    else: 
                        print(triangle[j][c], end=" ")
                        c-=1
                        j+=1
            except IndexError: 
                print("  ", end="")
            for k in range(i-h):
                print("  ", end="")
            print("")
print_triangle(5)