# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(example_list):
  def maximum(example_list):
    max = None
    for number in example_list:
      if max is None:
        max = number
      elif number > max:
        max = number
    maximum = f"The maximum is {max}."
    return maximum # better to return number and modify it outside (e.g., return max)
  def minimum(example_list):
    min = None
    for number in example_list:
      if min is None:
        min = number
      elif number < min:
        min = number
    minimum = f"The minimum is {min}."
    return minimum
  def average_sum(example_list):
    count = 0
    sum = 0
    for number in example_list:
      count = count + 1
      sum = sum + number
    tot_sum = sum
    average = sum / count
    avg_sum = f"The average is {average}. The sum is {tot_sum}."
    return avg_sum # return as tuple
  max_stats = maximum(example_list)
  min_stats = minimum(example_list)
  avg_sum_stats = average_sum(example_list)
  statistics = f"{max_stats} {min_stats} {avg_sum_stats}"
  return statistics

print(stats(example_list))

# Don't build the string inside the function. Return the number you need and then use it to build outside