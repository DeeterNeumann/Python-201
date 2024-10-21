# How can you call the function defined below using the given
# dictionary as its input.
# You shouldn't explicitly access the dict values, but use
# dictionary unpacking when passing the argument instead.

user = {"name": "Adelheid", "age": 22}

def congratulate(**user):
    happy_bday = ""
    for name, age in user.items():
        bday_wish = f"Today {name} is {age} years old.\nHappy Birthday!"
        happy_bday += bday_wish + "\n"
    return happy_bday
    
print(congratulate())



