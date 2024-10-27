# Reproduce the functionality of Python's built-in `enumerate()` function.
# Define a function called `my_enumerate()` that takes an iterable as input
# and gives back both the element as well as its index position as an integer.

def my_enumerate(list, start = 0):
    course_index = -1
    for course in courses:
        course_index += 1
        print(f"{course_index}: {course} Python")
        
courses = ['Intro', 'Intermediate', 'Advanced', 'Professional']

my_enumerate(courses)


# OUTPUT:
# 0: Intro Python
# 1: Intermediate Python
# 2: Advanced Python
# 3: Professional Python
