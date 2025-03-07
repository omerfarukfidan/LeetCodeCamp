"""
For example, imagine a queue at a trendy and fully booked restaurant.
 If you were trying to implement a fair system for seating guests,
  then you’d start by creating a queue and adding people as they arrive:
"""
#EXAMPLE OF QUEUE FIFO(First in First out)

from collections import deque


def create_queue():
    queue = deque()
    return queue


def append_new_customer_to_the_queue(name):
    queue.append(name)


def take_customer_inside_of_restaurant():
    return queue.popleft()

def show_me_the_queue():
    print(queue)

queue = create_queue()

append_new_customer_to_the_queue("Chris")
append_new_customer_to_the_queue("Jack")
append_new_customer_to_the_queue("Henrick")

print("Current QUEUE: ", end='')
show_me_the_queue()

take_customer_inside_of_restaurant()

print("Current QUEUE: ", end='')
show_me_the_queue()


