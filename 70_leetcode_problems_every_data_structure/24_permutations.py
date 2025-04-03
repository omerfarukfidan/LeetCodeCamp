"""
https://leetcode.com/problems/permutations/description/
46. Permutations
Medium
Topics
Companies
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]


Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
#VIDEO SOLUTION YOU NEED TO SOLVE BY YOURSELF 2.34.42

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, end):
            if start == end:
                result.append(nums[:])
                return
            for i in range(start, end):
                nums[start], nums[i] =  nums[i], nums[start]
                backtrack(start+1, end)
                nums[start], nums[i] =  nums[i], nums[start]

        result = []
        backtrack(0, len(nums))
        return result
