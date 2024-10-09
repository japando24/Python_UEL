# x va y khac vung nho vi list la kieu co kha nang mo rong
x = [1,2]
y = [1,2]
print(id(x))
print(id(y))
print(x == y)
print(x is y)

"""
Cac kieu du lieu khong co kha nang mo rong thi thuong cac bien tro cung 1 vung nho 
"""

#  a va b dang cung vung nho
a = 8
b = 8
print(id(a))
print(id(b))
print(a is b)
print(a == b)

# c va d cung vung nho
c = "str"
d = "str"
print(id(c))
print(id(d))
print(c == d)
print(c is d)

# attention to case that variables have big size
m = "p"*100
print(m)
n = "p"*100
print(n)
print(id(m)," ", id(n))
print(m == n)
m = "p"*1000000000
n = "p"*1000000000
print(id(m)," ", id(n))
print(m is n)

temp = "love"
s1 = temp + " python" # co vung nho rieng vi co them vung nho cua temp
s2 = "love" + " python"
print(id(s1), " ", id(s2))
print(s1 is s2) # False