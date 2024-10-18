# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.

def make_sandwich(bread, toppings):
    """Make a sandwich.
    
    Args:
        bread (str): Enter a type of bread e.g., wheat
        toppings (str): Enter any amount of toppings e.g., ham, cheese, mayo
    
    Returns:
        sammy = the type of bread on the bottom, toppings, and another slice of bread on top.
    """
    sammy = f"""
    {bread}
    {toppings}
    {bread}"""
    return sammy

print(make_sandwich("wheat", "turkey, bacon, cheddar, lettuce, tomatoes, peppers, avacado, mayo"))