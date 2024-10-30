# Reproduce the functionality of Python's built-in `enumerate()` function.
# Define a function called `my_enumerate()` that takes an iterable as input
# and gives back both the element as well as its index position as an integer.

courses = ['Intro', 'Intermediate', 'Advanced', 'Professional']

# indexes = list(range(len(courses)))

# print(indexes)

def my_enumerate(input_list):
    indexes = list(range(len(input_list)))
    enumerate_output_list = []
    for index, item in zip(indexes, input_list):
        enumerate_output_list.append((index, item))
    return enumerate_output_list

for i, c in my_enumerate(courses):
    print(f"{i}: {c} Python")


# OUTPUT:
# 0: Intro Python
# 1: Intermediate Python
# 2: Advanced Python
# 3: Professional Python
