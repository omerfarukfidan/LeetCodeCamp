"""
https://www.geeksforgeeks.org/reversing-first-k-elements-queue/

Reversing the first K elements of a Queue
Last Updated : 18 Mar, 2025
Given an integer k and a queue of integers, The task is to reverse the order of the first k elements of the queue, leaving the other elements in the same relative order.

Only following standard operations are allowed on the queue.

enqueue(x): Add an item x to rear of queue
dequeue(): Remove an item from the front of the queue
size(): Returns the number of elements in the queue.
front(): Finds front item.
Example:

Input: k = 3, Queue = 1 2 3 4 5
Output: 3 2 1 4 5
Explanation:  After reversing the first 3 elements from the given queue the resultant queue will be 3 2 1 4 5.


Input: k= 4, Queue = 4 3 2 1
Output: 1 2 3 4
Explanation: After reversing the first 4 elements from the given queue the resultant queue will be 1 2 3 4.


Table of Content

Approach 1 – Using the Recursion Call Stack – O(n) Time and O(n) Space
Approach – Using a Stack – O(n+k) Time and O(k) Space
Approach – Using Doubly Ended Queue – O(n+k) Time and O(k) Space
Approach 1 – Using the Recursion Call Stack – O(n) Time and O(n) Space
The idea is to remove and store the first k elements in recursive call stack and insert them in the queue in the reverse order then we can simply remove and add remaining items of the queue.
"""
# WATCH 3:38:05
