print("Enter your email: ", end="")
a = input()
print("Your email: ", a)

name = input("Enter your name: ")
grade = int(input("Enter your grade: "))
final = grade + 1
print("Name: "+ name + ", Grade: "+str(final))
print(f"Name: {name}, Grade: {final}")
print("Name {}, Grade {}".format(name, final))
print("Name {0}, Grade {1}".format(name, final))
print("Name {1}, Grade {0}".format(final, name))