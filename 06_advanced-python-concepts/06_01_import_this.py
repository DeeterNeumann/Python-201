# Add the necessary import statement in order to make this script
# produce output. Don't change any of the existing code.
# All the necessary variables and functions are
# already defined in the `codingnomads/` folder.

from codingnomads.ingredients import potato
import codingnomads.recipes.soup as s

soup = s.make_soup(potato)
print(soup)
