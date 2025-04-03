"""
https://neetcode.io/problems/anagram-groups
Group Anagrams
Solved
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.
"""

# 1st solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dictionary = {}  # defaultdict

        for index, s in enumerate(strs):
            srted = tuple(sorted(
                s))  # sorted() function returns a list and list is mutable but dictionary's key has to be immutable that is why tuple() needed
            if srted not in dictionary:
                dictionary[srted] = [s]
            else:
                dictionary[srted].append(s)

        retval = []
        for value in dictionary.values():
            retval.append(list(value))

        return retval

# 2nd solution doesn't work on leetcode but works fine on neetcode
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)

        for s in strs:
            sorted_s = tuple(sorted(s))
            dictionary[sorted_s].append(s)

        return dictionary.values()
