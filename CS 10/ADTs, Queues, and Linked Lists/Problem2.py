from collections import deque

class DequeQueue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)       # add to the back

    def dequeue(self):
        return self._items.popleft()   # remove from the front

    def peek(self):
        return self._items[0]          # look at the front without removing

    def is_empty(self):
        return len(self._items) == 0

#What does the following program print?

# Let's analyze the program step by step:
# 1. We create an instance of DequeQueue called q.
q = DequeQueue()

# 2. We enqueue "a" onto the queue.
# Running queue: "a"
q.enqueue("a")

# 2. We enqueue "b" onto the queue.
# Running queue: "a" <- "b"
q.enqueue("b")

# 3. We dequeue an item from the queue, which removes "a" and returns it.
# Running queue: "b"
# The output of this operation is "a".
print(q.dequeue())

# 4. We enqueue "c" onto the queue.
# Running queue: "b" <- "c"
q.enqueue("c")

# 5. We peek at the front of the queue, which is "b".
# The output of this operation is "b".
print(q.peek())

# 6. We dequeue an item from the queue, which removes "b" and returns it.
# Running queue: "c"
# The output of this operation is "b".
print(q.dequeue())

# 7. We dequeue an item from the queue, which removes "c" and returns it.
# Running queue: empty
# The output of this operation is "c".
print(q.dequeue())

# 8. We check if the queue is empty, which it is.
# The output of this operation is True.
# Print the result of is_empty() method.
print(q.is_empty())