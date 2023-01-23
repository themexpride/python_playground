"""
Data Structures - Lists - Queues

Queue
    List can be used as Queue
    Data Structure where FIFO

Why not use Queues?
    Not efficient
        inserts or pops from beginning of a list is slow

For an efficient Queue
    use collections.deque(list)
        fast appends and pops from both ends

Add items
    use append(item)

Remove items
    use popleft()
"""

from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)
