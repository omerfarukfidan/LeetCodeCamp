"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

108. Convert Sorted Array to Binary Search Tree
Easy
Topics
Companies
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.



Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
"""
# 04:21:07
# VIDEO SOLUTION
from collections import deque


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        n = len(nums)
        mid = n // 2
        root = TreeNode(nums[mid])

        q = deque()
        q.append((root, 0, mid - 1))
        q.append((root, mid + 1, n - 1))

        while q:
            parent, left, right = q.popleft()
            if left <= right:
                mid = (left + right) // 2
                child = TreeNode(nums[mid])
                if nums[mid] < parent.val:
                    parent.left = child
                else:
                    parent.right = child
                q.append((child, left, mid - 1))
                q.append((child, mid + 1, right))

        return root


# MY TRY BUT NOT WORKING AND WRONG SOLUTION
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        mid = nums[len(nums) // 2]
        left_nums = nums[:(len(nums) // 2)]
        right_nums = nums[(len(nums) // 2) + 1:]

        left_queue = deque(left_nums)
        right_queue = deque(right_nums)

        BST = TreeNode(mid)
        if left_queue:
            left_tree = TreeNode(left_queue.pop())
            while left_queue:
                val = left_queue.pop()
                if left_tree.val < val:
                    left_tree = left_tree.left
                    left_tree = TreeNode(val)
            BST.left = left_tree

        if right_queue:
            right_tree = TreeNode(right_queue.pop())
            while right_queue:
                val = right_queue.pop()
                if right_tree.val > val:
                    right_tree = right_tree.left
                    right_tree = TreeNode(val)
            BST.right = right_tree

        return BST

