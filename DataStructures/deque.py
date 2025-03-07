"""
Linked lists serve a variety of purposes in the real world.
 They can be used to implement (spoiler alert!) queues or stacks as well as graphs.

They’re also useful for much more complex tasks,
 such as lifecycle management for an operating system application.

In Python, there’s a specific object in the collections module
 that you can use for linked lists called deque (pronounced “deck”),
 which stands for double-ended queue.

collections.deque uses an implementation of a linked list in which you can access,
 insert, or remove elements from the beginning or end of a list with constant O(1) performance.



"""

from collections import deque

llist = deque()

llist.append("A")
llist.append("B")

print(llist)

print(llist.popleft())

llist.append("C")

print(llist)

print(llist.pop())

print(llist)

llist.appendleft("D")

print(llist)
