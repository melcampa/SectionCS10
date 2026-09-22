# There's no built-in product function the way there's a built-in sum. Write a one line 
# expression, using the reduce function from the functools module, that computes the 
# product of all the numbers in nums. 
# 

nums = [2, 3, 4, 5]

# We know that we need to use the reduce function, which takes two arguments: 
# a function and an iterable. 
# Let's import the reduce function from the functools module first.

from functools import reduce

# Now we can use reduce to compute the product of all the numbers in nums.

product = reduce(lambda x, y: x * y, nums)

# Reduce here combines two elements at a time, multiplying them together, 
# and continues this process until all elements have been combined into a single product.

print("The product of all numbers in nums is:", product)