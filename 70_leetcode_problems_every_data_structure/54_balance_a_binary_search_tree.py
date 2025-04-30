"""
https://leetcode.com/problems/balance-a-binary-search-tree/description/

1382. Balance a Binary Search Tree
Medium
Topics
Companies
Hint
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.



Example 1:


Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
Example 2:


Input: root = [2,1,3]
Output: [2,1,3]


Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 105
"""
# 04:34:01
# LEETCODE SOLUTION -> https://leetcode.com/problems/balance-a-binary-search-tree/solutions/5370661/python-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def in_order_traversal(node):
            if not node:
                return []
            return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)

        sorted_values = in_order_traversal(root)

        def build_balanced_bst(values):
            if not values:
                return None

            mid = len(values) // 2

            root = TreeNode(values[mid])
            root.left = build_balanced_bst(values[:mid])
            root.right = build_balanced_bst(values[mid + 1:])
            return root

        return build_balanced_bst(sorted_values)

