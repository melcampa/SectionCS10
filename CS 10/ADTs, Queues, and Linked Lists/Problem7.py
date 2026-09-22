class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = self
        self.prev = self

class LinkedList:
    def __init__(self):
        self.sentinel = Node()

    def append(self, value):
        node = Node(value)
        last = self.sentinel.prev
        node.prev, node.next = last, self.sentinel
        last.next = node
        self.sentinel.prev = node

    def prepend(self, value):
        node = Node(value)
        first = self.sentinel.next
        node.prev, node.next = self.sentinel, first
        first.prev = node
        self.sentinel.next = node

    def __iter__(self):
        cur = self.sentinel.next
        while cur is not self.sentinel:
            yield cur.value
            cur = cur.next

    def __str__(self):
        return " -> ".join(str(v) for v in self)

# Starting from an empty LinkedList (as described in this lecture), 
# trace through this sequence of calls:

# Let's analyze the sequence of calls step by step:
# 1. We create an empty LinkedList called lst.
lst = LinkedList()

# 2. We append the value 10 to the list.
# The list now contains: 10 -> (sentinel)
lst.append(10)

# 3. We prepend the value 5 to the list.
# The list now contains: 5 -> 10 -> (sentinel)
lst.prepend(5)

# 4. We append the value 20 to the list.
# The list now contains: 5 -> 10 -> 20 -> (sentinel)
lst.append(20)

# Afterward, what are the values in the list, in order? 

# The values in the list, in order, are: 5, 10, 20.
# Note that the sentinel node is not included in the output, as it is a placeholder 
# and does not hold a meaningful value.

print(lst)  # This will print the list in order


# What does lst.sentinel.next.value equal? What does lst.sentinel.prev.value equal?
# lst.sentinel.next.value equals 5 (the first value in the list)
print(lst.sentinel.next.value)  # Output: 5

# lst.sentinel.prev.value equals 20 (the last value in the list)
print(lst.sentinel.prev.value)  # Output: 20