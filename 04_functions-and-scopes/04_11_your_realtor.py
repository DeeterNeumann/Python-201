# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.

def house_list(**kwargs):
    listings = ""
    for house, amenities in kwargs.items():
        description = f"{house}: {amenities}"
        listings += description + "; "
    return listings

print(house_list(Union_Street = "ground floor, loft, single bathroom, half shower", Cedar_Street = "7th floor, two bedroom, large patio, hot tub"))