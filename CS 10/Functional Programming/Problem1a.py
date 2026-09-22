bookstore_inventory = [ ("To Kill a Mockingbird", 2, "Fiction", 281), 
                        ("1984", 3, "Fiction", 328), 
                        ("Pride and Prejudice", 1, "Fiction", 426)]

# What do we know?
# We have a list of tuples, where each tuple contains a book title, its corresponding 
# quantity in stock, genre, and number of pages in the format 
# (title, quantity, genre, pages).

# We have:
# - 2 copies of "To Kill a Mockingbird", which is a Fiction book with 281 pages
# - 3 copies of "1984", which is a Fiction book with 328 pages  
# - 1 copy of "Pride and Prejudice", which is a Fiction book with 426 pages

# What do we need to know?
# We need to sort the inventory by pages in ascending order to see which books 
# have the least number of pages. We also want to filter the inventory to only 
# include books above 300 pages.

# We can use the `sorted()` function with a custom key to sort the list of tuples
# based on the number of pages, and we can use a list comprehension to filter
# the inventory to only include books with more than 300 pages.

filtered_inventory = [item for item in bookstore_inventory if item[3] > 300]
filtered_inventory.sort(key=lambda item: item[3])