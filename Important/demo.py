"""
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

#MY SOLUTION
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
A = [1, 3, 6, 4, 1, 2]

def solution(A):
    new_A = set(A)
    for i in range(1, 100000):
        if i not in new_A:
            return i
print(solution(A))

"""
from random import randrange
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
A = []
x = [A.append(i) for i in range (1,10000)]# append doesnt return anything
print(A)
A.pop(randrange(10000))
def solution(A):
    new_A = set(A)
    for i in range(1, 100000):
        if i not in new_A:
            return i
print(solution(A))



