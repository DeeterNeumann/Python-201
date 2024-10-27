# Add type annotations to the three functions shown below.
# use the type and the arrow? e.g., def greet(greeting: str, name: str) -> str:

def multiply(num1: int, num2: int) -> int:
    return num1 * num2

def greet(greeting: str, name: str) -> str:
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

def shopping_list(*args) -> None:
    [print(f"* {item}") for item in args]

# pylint linter