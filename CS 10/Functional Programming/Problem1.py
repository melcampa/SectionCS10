bookstore_inventory = [("To Kill a Mockingbird", 2), ("1984", 3), ("Pride and Prejudice", 1)]

# What do we know?
# We have a list of tuples, where each tuple contains a book title and its corresponding 
# quantity in stock in the format (title, quantity).

# We have:
# - 2 copies of "To Kill a Mockingbird"
# - 3 copies of "1984"
# - 1 copy of "Pride and Prejudice"

# What do we need to know?
# We need to sort the inventory by quantity in descending order to see which books 
# have the most stock available.

# We can use the `sorted()` function with a custom key to sort the list of tuples 
# based on the quantity.

bookstore_inventory.sort(key=lambda item: item[1], reverse=True)

print("Sorted Book Inventory by Quantity (Descending):")
for title, quantity in bookstore_inventory:
    print(f"{title}: {quantity} copies")