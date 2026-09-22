#Rewrite the following as a simple list comprehension:

words = ["cat", "elephant", "ox", "giraffe", "newt"]
result = list(map(lambda w: w.lower(), filter(lambda w: len(w) > 4, words)))

# What do we know?
# We have a list of words called `words`.
# We know that we are using the `filter()` function to keep only the words 
# with a length greater than 4.
# We are then using the `map()` function to convert those words to lowercase.
# We can rewrite this as a simple list comprehension:

result = [w.lower() for w in words if len(w) > 4]
# Breaking it down...
# w.lower() is the expression that converts each word to lowercase.
# for w in words is the iteration over each word in the list.
# if len(w) > 4 is the condition that filters the words.

# Note that "cat" and "ox" are not included in the final result because 
# their lengths are not greater than 4.

print("The filtered and lowercased words are:", result)
