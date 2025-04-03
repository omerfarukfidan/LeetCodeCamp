"""
https://neetcode.io/problems/top-k-elements-in-list
Top K Frequent Elements
Solved
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.

"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        list_map = []
        for key, value in hashmap.items():
            list_map.append((key, value))

        sorted_by_second = sorted(list_map, key=lambda tup: tup[1], reverse=True)  # sorting tuples
        # sorting by value dict(sorted(people.items(), key=lambda item: item[1]))

        # print(sorted_by_second)

        retval = []
        for i in range(k):
            retval.append(sorted_by_second[i][0])

        return retval


"""
HELPFUL RESOURCES
How to sort a list/tuple of lists/tuples by the element at a given index -> https://stackoverflow.com/questions/3121979/how-to-sort-a-list-tuple-of-lists-tuples-by-the-element-at-a-given-index
**** 
sorted_by_second = sorted(data, key=lambda tup: tup[1])
****


Sorting Dictionaries in Python -> https://realpython.com/sort-python-dictionary/
****
people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}
# Sort by key
dict(sorted(people.items())) # output will be {1: 'Jill', 2: 'Jack', 3: 'Jim', 4: 'Jane'}
# Sort by value
dict(sorted(people.items(), key=lambda item: item[1])) #output will be {2: 'Jack', 4: 'Jane', 1: 'Jill', 3: 'Jim'}
****


Sort in Descending Order by sorted() method -> https://www.programiz.com/python-programming/methods/built-in/sorted
**** 
sorted_numbers = sorted(numbers, reverse=True)
****

Get key by value in dictionary -> https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary
**** 
mydict = {'george': 16, 'amber': 19}
print(list(mydict.keys())[list(mydict.values()).index(16)])  # Prints george
****

"""
