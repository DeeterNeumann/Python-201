# Add a Google-style docstring to the function below. Your docstring
# should at least describe what it does, what arguments it takes,
# and what it returns.

def km_to_miles(km):
    """Converts kilometers to miles.
    
    Args:
        km (int): distance in kilometers, e.g., 6 
    
    Returns:
        miles (int): distance in miles
    """
    miles = km * 0.6
    return miles

print(km_to_miles.__doc__)
