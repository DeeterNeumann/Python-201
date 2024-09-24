# Write a script that creates a dictionary of keys, `n`
# and values `n * n` for numbers 1 to 10. For example:
# result = {1: 1, 2: 4, 3: 9, ... and so on}

keys_squared = {}

n = 1

while n < 11:
    keys_squared[n] = n*n
    n += 1

print(keys_squared)