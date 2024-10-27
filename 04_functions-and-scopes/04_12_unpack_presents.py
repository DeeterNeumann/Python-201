# How can you call the function defined below using the given
# dictionary as its input.
# You shouldn't explicitly access the dict values, but use
# dictionary unpacking when passing the argument instead.


def congratulate(name, age, cake = "vanilla"): # if no default, then it would have to be inputted
    bday_wish = f"Today {name} is {age} years old.\nHappy Birthday!\nWe're having {cake} cake."
    return bday_wish # just return in line 8 rather than assigning variable and calling it

user = {"name": "Adelheid", "age": 22}

print(congratulate(**user))

users = [{"name": "Adelheid", "age": 22, "cake": "chocolate"}, {"name": "Deeter", "age": 26, "cake": "chocolate"}]

for user in users:
    print(congratulate(**user))