"""
https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/

530. Minimum Absolute Difference in BST
Easy
Topics
Companies
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.



Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1


Constraints:

The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105


Note: This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
"""
# VIDEO SOLUTION
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float(+inf)
        prev_val = float(-inf)

        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                min_diff = min(min_diff, root.val - prev_val)
                prev_val = root.val
                root = root.right
        return min_diff


# MY SOLUTION 19.04.2025
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        node = root
        min_diff = float('inf')
        stack = []
        values = []
        while node or stack:
            if node:
                stack.append(node)
                values.append(node.val)
                node = node.left
            else:
                node = stack.pop()
                node = node.right

        values.sort()

        for i in range(len(values) - 1):
            diff = abs(values[i] - values[i + 1])
            min_diff = min(diff, min_diff)

        return min_diff

