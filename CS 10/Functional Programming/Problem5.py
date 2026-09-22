
# In a sentence or two, explain why sum(x ** 2 for x in range(10_000_000)) 
# uses much less memory than sum([x ** 2 for x in range(10_000_000)]), even 
# though both compute the same final sum.


# Let's look at the first example:
sum1 = sum(x ** 2 for x in range(10_000_000))

# In this case, we are using a generator expression (x ** 2 for x in range(10_000_000)).
# A generator expression computes each value on-the-fly, yielding one value at a time.
# Memory is not allocated for all the computed values at once, which makes it more 
# memory-efficient for large computations.

# Now, let's look at the second example:
sum2 = sum([x ** 2 for x in range(10_000_000)])

# In this case, we are using a list comprehension ([x ** 2 for x in range(10_000_000)]).
# A list comprehension creates a list in memory that contains all the computed values at 
# once. Memory is allocated for the entire list, which can be quite large for 
# 10 million elements.

# Therefore, the first example uses much less memory because it does not store all the 
# computed values in memory at once, while the second example does. 
# The generator expression is more memory-efficient for large computations.