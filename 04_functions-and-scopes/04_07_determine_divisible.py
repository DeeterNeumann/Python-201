# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages

number  = int(input("Enter a number between 1 and 1,000,000,000: "))

def or_and(number):
    def div_4_or_7(number):
        if number % 4 == 0 or number % 7 == 0:
            four_or_seven = True
        else:
            four_or_seven = False
        result_or = f"Is {number} divisible by 4 or 7?: {four_or_seven}."
        return result_or

    def div_4_and_7(number):
        if number % 4 == 0 and number % 7 == 0:
            four_and_seven = True
        else:
            four_and_seven = False
        result_and = f"Is {number} divisible by 4 and 7?: {four_and_seven}."
        return result_and
    
    result_or = div_4_or_7(number)
    result_and = div_4_and_7(number)
    
    results = f"{result_or} {result_and}"
    return results

print(or_and(number))