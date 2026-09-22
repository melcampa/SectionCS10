# Demo: what goes wrong if a linked queue's dequeue() forgets to reset `back`.



class Node:
    # One link in the chain: a value plus a pointer to the next node.

    def __init__(self, value):
        self.value = value
        self.next = None  # nothing behind this node yet


class LinkedQueue:
    # The CORRECT queue.

    def __init__(self):
        # A new queue is empty, so both references are None.
        self.front = None
        self.back = None

    def enqueue(self, value):
        node = Node(value)  # wrap the value in a new node

        if self.back is None:
            # Empty queue: the new node is BOTH the front and the back.
            # (Here we use `back is None` to mean "the queue is empty".)
            self.front = node
        else:
            # Non-empty queue: hook the new node onto the end of the chain.
            self.back.next = node

        # Either way, the new node is now the last one in line.
        self.back = node

    def dequeue(self):
        if self.front is None:
            raise IndexError("dequeue from empty queue")

        value = self.front.value       # remember what we're removing
        self.front = self.front.next   # move `front` one node forward

        # If that was the last node, `front` is now None (queue is empty).
        # `back` STILL points at the node we just removed, so we must clear
        # it too. These two lines are what the buggy version below is missing.
        if self.front is None:
            self.back = None

        return value


class BuggyLinkedQueue(LinkedQueue):
    # Same as LinkedQueue, except dequeue() never touches `back`.

    # (Subclassing lets us reuse __init__ and enqueue unchanged, so the ONLY
    # difference between the two classes is the missing cleanup in dequeue.)
    
    def dequeue(self):
        if self.front is None:
            raise IndexError("dequeue from empty queue")

        value = self.front.value
        self.front = self.front.next   # if this was the last node, front = None
        # BUG: `back` is never reset, so it may now point at a removed node.
        return value


def scenario(queue_cls):
    #Run the tricky sequence: enqueue, dequeue (empties queue), enqueue.
    q = queue_cls()

    q.enqueue(3)    # one node: front and back both point at it
    q.dequeue()     # removes it, so the queue is empty again
    # Buggy version: front is None (empty) but back is NOT None (stale node).
    print(f"  after dequeue:    front={q.front}, back is stale node: {q.back is not None}")

    q.enqueue(5)
    # Buggy version: enqueue sees back is not None, so it thinks the queue is
    # non-empty and attaches the new node to the REMOVED node's `next`.
    # It never sets `front`, so front stays None and the new node is orphaned.
    print(f"  after enqueue(5): front={q.front}, back.value={q.back.value}")

    try:
        # dequeue starts at `front`. If that's None, it never follows any
        # links, so it can't find the orphaned node holding 5.
        print(f"  dequeue() -> {q.dequeue()}")
    except IndexError as e:
        print(f"  dequeue() -> IndexError: {e}")


# Run the same scenario on both versions and compare the output.
for cls in (BuggyLinkedQueue, LinkedQueue):
    print(cls.__name__)
    scenario(cls)

# Handy check for spotting this bug: front and back should be None together.
#     assert (q.front is None) == (q.back is None)
# The buggy queue fails this right after the first dequeue().