# Using a list comprehension, create a *cartesian product* (google this!)
# of the given lists. Then open up your online shop ;)

#from itertools import product

colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]

t_shirt_shop = [(color, size) for color in colors for size in sizes]

print(t_shirt_shop)