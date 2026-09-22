#ADT: the promises (what operations exist and how they behave).
#Data structure: a concrete way to keep those promises (how it's stored).


from collections import deque


# --- The ADT: only the promises, no implementation --------------------------
class Queue:
    """Queue ADT: first in, first out."""

    def enqueue(self, item): ...   # add to the back
    def dequeue(self): ...         # remove and return the front
    def peek(self): ...            # look at the front without removing
    def is_empty(self): ...        # True if nothing is stored


# --- Data structure #1: built on collections.deque (O(1) dequeue) -----------
class DequeQueue(Queue):
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        return self._items.popleft()

    def peek(self):
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0


# --- Data structure #2: built on a plain list (O(n) dequeue) ----------------
class ListQueue(Queue):
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        return self._items.pop(0)   # shifts every remaining item left

    def peek(self):
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0


# --- Code that uses only the ADT's interface --------------------------------
# INPUT: a queue (any implementation)
# OUTPUT: a list of the served customers
def serve_customers(q):
    q.enqueue("Ann")
    q.enqueue("Bo")
    q.enqueue("Cy")
    served = []
    while not q.is_empty():
        served.append(q.dequeue())
    return served


if __name__ == "__main__":
    # Same behavior, different internals.
    print(serve_customers(DequeQueue()))   # ['Ann', 'Bo', 'Cy']
    print(serve_customers(ListQueue()))    # ['Ann', 'Bo', 'Cy']
