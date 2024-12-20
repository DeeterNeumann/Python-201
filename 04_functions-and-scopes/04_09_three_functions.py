# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.

def grocery_list(meat, *sides):
    grocery_list = join_sides(sides)
    groceries = f"{meat}, {grocery_list}"
    return groceries

def recipe(meat, *sides):
    """Make a meal.
    
    Args:
        meat (str): Enter a type of meat e.g., chicken
        sides (str): Enter any amount of sides e.g., corn, potatoes, pasta
    
    Returns:
        dinner = the type of bread on the bottom, toppings, and another slice of bread on top.
    """
    side_dish = join_sides(sides) #only works with list of strings or items that can be turned into strings
    dish = f"{meat} with {side_dish}"
    return dish

def dinner_invite(name, main, *sides):
    groceries = grocery_list(main, *sides)
    dish = recipe("chicken", *sides)
    invite = f"{name}, please join us for {dish}. I've picked up the {groceries}."
    return invite

def join_sides(sides):
    return ", ".join(sides)

sides = "corn, potatoes, asparagus".replace(" ", "").split(",")

print(dinner_invite("Watson", "chicken", *sides))