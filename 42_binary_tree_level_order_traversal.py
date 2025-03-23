"""
https://leetcode.com/problems/binary-tree-level-order-traversal/description/
102. Binary Tree Level Order Traversal
Medium
Topics
Companies
Hint
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""
# VIDEO SOLUTION
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        retval = []

        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()

                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            retval.append(level)

        return retval


# MY TRY BUT NOT WORKING PROPERLY
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])

        retval = []
        retval.append([root.val])
        while queue:
            temp = []
            node = queue.popleft()

            if not node.left and not node.right and len(queue) == 0:
                break

            if node.left and node.right:
                queue.append(node.left)
                queue.append(node.right)
                temp.append(node.left.val)
                temp.append(node.right.val)
            elif node.right:
                queue.append(node.right)
                temp.append(node.right.val)
            elif node.left:
                queue.append(node.left)
                temp.append(node.left.val)
            if len(temp) != 0:
                retval.append(temp)

        return retval
