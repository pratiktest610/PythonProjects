# Absolute Path
with open("C:/Users/geeta/Downloads/data.txt") as file:
    msg = file.read()
print(msg)

# Relative path
with open("../../Downloads/data.txt") as file2:
    msg = file2.read()
print(msg)


