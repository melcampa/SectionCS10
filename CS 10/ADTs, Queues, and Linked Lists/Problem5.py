# Write a function count_nodes(head) that takes a reference to the first node of 
# a chain of Node objects (as described in this lecture — each with a .value and a .next) 
# and returns how many nodes are in the chain. Do not modify the chain.

# Let's implement the count_nodes function as described:
# We will traverse the linked list starting from the head node, counting each node until we
# reach the end of the list (when the current node is None).
# We will return the count of nodes at the end.

def count_nodes(head):
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next
    return count