# How can you call the function defined below using the given
# dictionary as its input.
# You shouldn't explicitly access the dict values, but use
# dictionary unpacking when passing the argument instead.


def congratulate(name, age):
    bday_wish = f"Today {name} is {age} years old.\nHappy Birthday!"
    return bday_wish

user = {"name": "Adelheid", "age": 22}

print(congratulate(**user))



