"""
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/

Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.



Example 1:


Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Example 2:


Input: root = [5,3,6,2,4,null,7], k = 28
Output: false


Constraints:

The number of nodes in the tree is in the range [1, 104].
-104 <= Node.val <= 104
root is guaranteed to be a valid binary search tree.
-105 <= k <= 105
"""
# 4:26:29
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = set()

        q = deque([root]) #queue take what kind of inputs? iterable?

        while q:
            node = q.popleft()
            if (k - node.val) in nums:
                return True
            else:
                nums.add(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return False


"""
---
✅ `deque([root])` — What Does It Accept?

The `deque()` function expects an **iterable** as its argument.

🔹 Example:
from collections import deque

q = deque([root])  # root is a single element inside a list
```

- `[root]` → This is a **list**, which is **iterable**
- So `deque([root])` means:  
  ➜ “Create a queue containing one element: `root`”

---
❌ Can You Write `deque(root)`?

No — because `root` (e.g., a `TreeNode` object) is **not iterable** by itself.  
You would get this error:

TypeError: 'TreeNode' object is not iterable
```

---
🧠 What Types of Elements Can You Put Inside a `deque`?

| Type               | Iterable? | Mutable? | Allowed in `deque`?                |
|--------------------|-----------|----------|-------------------------------------|
| `list`             | ✅        | ✅       | ✅ (as elements or as the iterable itself) |
| `int`, `float`     | ❌        | ❌       | ✅ if wrapped in iterable like `[1]` |
| `str`              | ✅        | ❌       | ✅ (but split character by character) |
| `TreeNode` (custom object) | ❌ | ✅/❌  | ✅ if wrapped like `[root]`         |
| `tuple`, `set`     | ✅        | tuple ❌ / set ✅ | ✅                             |

---
💡 Can the elements inside a `deque` be mutable?

**Yes! Absolutely.**  
`deque` does not care about the mutability of the objects inside it.  
You can store anything: numbers, strings, lists, objects — even other deques.

---

📌 Summary:

| Question                             | Answer                                 |
|--------------------------------------|----------------------------------------|
| What does `deque(...)` require?      | An **iterable**                        |
| Will `deque(root)` work?             | ❌ No, if `root` is not iterable       |
| Why does `deque([root])` work?       | Because `[root]` is a list (iterable) |
| Can `deque` hold mutable objects?    | ✅ Yes                                  |

---
"""
