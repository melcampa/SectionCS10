from functools import reduce

nums = [2, 3, 4, 5]
product = reduce(lambda x, y: x * y, nums)

# Let's do some more complicated examples to see how reduce works.

# Example 1: Find the maximum value in a list.
max_value = reduce(lambda x, y: x if x > y else y, nums)
print(max_value)

# Example 2: Concatenate a list of strings.
strings = ["Hello", " ", "World", "!"]
concatenated_string = reduce(lambda x, y: x + y, strings)
print(concatenated_string)

# Example 3: Compute the factorial of a number using reduce.
n = 5
factorial = reduce(lambda x, y: x * y, range(1, n + 1))
print(f"The factorial of {n} is: {factorial}")
