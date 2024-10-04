def generate_pascals_triangle(n): 
    triangle = [[1]]
    for i in range(1, n): 
        row=[1]
        for j in range(1, i): 
            row.append(triangle[i-1][j-1] + triangle[i-1][j]+1)
        row.append(1)
        triangle.append(row)
    return triangle
def print_update_down_pascals_triangle(h): 
    triangle = generate_pascals_triangle(h)

    for i in range (h-1, -1, -1): 
        print(" "*(h-i-1), end="")
        for num in triangle[i]:
            print(num, end=" ")
        print()

print_update_down_pascals_triangle(5) 
