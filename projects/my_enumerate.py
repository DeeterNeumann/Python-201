# Reproduce the functionality of Python's built-in `enumerate()` function.
# Define a function called `my_enumerate()` that takes an iterable as input
# and gives back both the element as well as its index position as an integer.

courses = ['Intro', 'Intermediate', 'Advanced', 'Professional']

def my_enumerate(list):
    indexes = range(len(courses))
    for index, course in zip(indexes, courses):
        (i, c) = (index, course)
        course_offering = print(f"{i}: {c} Python")
    return course_offering

my_enumerate(courses)


# OUTPUT:
# 0: Intro Python
# 1: Intermediate Python
# 2: Advanced Python
# 3: Professional Python
