"""
https://leetcode.com/problems/search-in-a-binary-search-tree/

700. Search in a Binary Search Tree
Easy
Topics
Companies
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.



Example 1:


Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
Example 2:


Input: root = [4,2,7,1,3], val = 5
Output: []


Constraints:

The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 107
root is a binary search tree.
1 <= val <= 107
"""
# MY SOLUTION SAME WITH VIDEO
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        while root:
            if root.val == val:
                return root
            elif root.val < val:
                root = root.right
            else:
                root = root.left

        return None
"""
In Python, when you pass an argument to a function, you're passing a reference to the same object in memory, not the actual object itself. This means:

Mutable objects (e.g., lists, dictionaries):
Changes made to the object inside the function will affect the original object outside the function.

Immutable objects (e.g., integers, strings, tuples):
Since these objects cannot be changed, any modification inside the function creates a new object.
The original object remains unchanged.

---
✅ Passing mutable objects:

def modify_list(lst):
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]
---

---
❌ Passing immutable objects:

def modify_number(num):
    num += 1

my_num = 5
modify_number(my_num)
print(my_num)  # Output: 5
---


--------------------------------------------------------------------------------------
✅ Mutable objects → Can be changed
Lists, dictionaries, and sets are mutable.

When you pass them to a function, you're passing a reference to the same object.

So, any modification will affect the original object.

Example:
---
def add_item(lst):
    lst.append(99)

my_list = [1, 2]
add_item(my_list)
print(my_list)  # ➜ [1, 2, 99]
# my_list was modified because list is mutable.
---

❌ Immutable objects → Cannot be changed
Integers, strings, and tuples are immutable.

When passed to a function, you're still passing a reference, but...

If you try to modify it, Python creates a new object (a copy), and the original stays the same.

Example:
---
def increase(num):
    num += 1  # This creates a new integer object

x = 10
increase(x)
print(x)  # ➜ 10
# x didn't change because int is immutable. num += 1 created a new object.
---

💡 Summary to Remember:
Type	What Happens When Modified?
Mutable	Modifies the original object directly
Immutable	Creates a new copy; original stays unchanged

"""
