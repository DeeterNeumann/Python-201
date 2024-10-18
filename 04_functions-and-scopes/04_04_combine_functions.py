# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.


def write_letter(greeting, name, text):
    def greet(greeting):
        sentence = f"{greeting}, {name}! How are you?"
        return sentence
    letter = greet(greeting) + f" {text}. Goodbye, {name}."
    return letter

print(write_letter("Hello", "Deeter", "Did you figure out how to get this code to work?"))