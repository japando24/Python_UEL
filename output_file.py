with open("output.txt", "w") as f:
    f.write("Hello, this is an output to file!")
with open("output.txt", "r") as f:
    print(f.read())
