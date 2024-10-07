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
    triangle = generate_pascals_triangle(h)
    for i in range(2*h, 1):
        if i >= h: 
            j = 0 
            c = i//2
            for k in range(i-h): 
                print("  ", end="")
            while j < (2*h - i): 
                if (i%2 == 0 and j%2 == 0) or (i%2 == 1 and j%2 == 1):
                    print("   ", end="")
                    if j == 0: 
                        pass 