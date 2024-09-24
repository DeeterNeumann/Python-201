# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list_ = [1, 2, 3, 4, 3, 4, 5]

dups_gone = set(list_)

print(dups_gone)

dups_gone_again = []

for n in list_:
    if n not in dups_gone_again:
        dups_gone_again.append(n)

print(dups_gone_again)
