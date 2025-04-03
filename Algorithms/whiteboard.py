
"""
ONE LINE FOR LOOP WITH APPEND:
ten_times_one = [1 for i in range(10)]
print(ten_times_one)

one_to_ten = [x for x in range(1,11)]
print(one_to_ten)
-------------------------------------------------------------
DICTIONARIES(MAPS):
my_dict = {}
for i in range(10):
    my_dict[i] = i+1
print("keys:", my_dict.keys())
print("values:", my_dict.values())
print("my_dict:", my_dict.items())

-------------------------------------------------------------
FIBONACCI WITH RECURSION
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(5))


-------------------------------------------------------------
HOW TO REACH AN INDEX BY VALUE
nums = [2,3,4,1]
print(nums.index(4)) # it returns 2

-------------------------------------------------------------
TWO POINTERS VS SLIDING WINDOW
-> If you're tracking a condition over a range, use Sliding Window.
* Finding max/min/average of subarrays
* Keeping track of unique characters or frequency
* Optimal subarray/subsequence tracking

1. Fixed-size window:
left = 0
right = 0
📌 Used when window size k is known:
k = 3
while right < len(arr):
    window_sum += arr[right]
    if right - left + 1 == k:
        max_sum = max(max_sum, window_sum)
        window_sum -= arr[left]
        left += 1
    right += 1

2. Variable-size window:
left = 0
for right in range(len(arr)):
    # Expand window with arr[right]
    # If condition not met, shrink window
    while condition_not_met:
        left += 1
📌 Used when looking for smallest/largest valid window:
# Minimum window that has sum >= target
window_sum = 0
min_len = float('inf')
left = 0

for right in range(len(arr)):
    window_sum += arr[right]
    while window_sum >= target:
        min_len = min(min_len, right - left + 1)
        window_sum -= arr[left]
        left += 1

->If you're comparing or scanning, especially in sorted arrays, use Two Pointers.
* Searching in sorted arrays (like two_sum)
* Reversing arrays/strings
* Comparing values from different ends
* Detecting duplicates or pairs

1. Same Direction (one pointer chases the other):
left = 0
right = 1  # usually starts just ahead of left
📌 Used when comparing elements in a sequence (like duplicates or pairs):
while right < len(arr):
    if arr[left] == arr[right]:
        return True
    left += 1
    right += 1

2. Opposite Ends (start from both sides):
left = 0
right = len(arr) - 1
📌 Used when the array is sorted or you want to close in:
while left < right:
    if arr[left] + arr[right] == target:
        return [left, right]
    elif arr[left] + arr[right] < target:
        left += 1
    else:
        right -= 1

-------------------------------------------------------------


-------------------------------------------------------------


-------------------------------------------------------------


-------------------------------------------------------------
"""


