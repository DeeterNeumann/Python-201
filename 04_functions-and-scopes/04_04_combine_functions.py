# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.


# def write_letter(greeting, name, text):
#     def greet(greeting):
#         sentence = f"{greeting}, {name}! How are you?"
#         return sentence
#     letter = greet(greeting) + f" {text}. Goodbye, {name}."
#     return letter

# print(write_letter("Hello", "Deeter", "Did you figure out how to get this code to work?"))

# instead of nesting, write two separate functions making sure to pass name into greet and write_letter
# preferred way is to write functions separately unless function is doing something very specific (even if valid Python)

def greet(greeting, name):
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

def write_letter(greeting, name, text):
    letter = greet(greeting, name) + f" {text}. Goodbye, {name}."
    return letter

print(write_letter("Hello", "Deeter", "Did you figure out how to get this code to work?"))
