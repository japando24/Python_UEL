import math
def distance(A, B):
    return math.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)
try:
    xA = int(input("Enter xA: "))
    yA = int(input("Enter yA: "))
    A = [xA,yA]
    xB = int(input("Enter xB: "))
    yB = int(input("Enter yB: "))
    B = [xB, yB]
    print("Distance between A and B: ", distance(A,B))
except ValueError:
    print(ValueError)