# List comprehension (for creating new list from existing sequences(list/strings/tuple/etc(where index matters)) without using loop)
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "pratik"
letters = [letter for letter in name]
print(letters)

range_2x = [n*2 for n in range(1, 5)]
print(range_2x)

# conditional list comprehensions
names = ["alex", "beth", "caroline", "dave", "eleanor", "freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names_upper = [name.upper() for name in names if len(name) > 5]
print(long_names_upper)
