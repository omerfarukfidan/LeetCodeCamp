"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5


Constraints:

The number of nodes in the tree is in the range [0, 105].
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])

        while queue:
            node, level = queue.popleft()

            if node.left == None and node.right == None:
                return level

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return 0


"""
💡 Iterable vs. Non-Iterable in Python

| Data Type     | Iterable? | Explanation |
|---------------|-----------|-------------|
| `list`        | ✅         | Can be looped over with a `for` loop |
| `tuple`       | ✅         | Iterable but immutable |
| `set`         | ✅         | Unordered, unique elements, and iterable |
| `dict`        | ✅         | Iterable over keys by default |
| `str`         | ✅         | Iterable character by character |
| `int`, `float`| ❌         | Not iterable – cannot be used directly in a `for` loop |
| `None`        | ❌         | Not iterable |
| `TreeNode`    | ❌         | Not iterable unless you explicitly define an iterator |

---
🧠 Common Parenthesis & Iterable Pitfalls

| Syntax             | Meaning / Explanation                            |
|--------------------|--------------------------------------------------|
| `(1)`              | Just an `int` – parentheses have no effect here |
| `(1,)`             | Single-element `tuple` ✔️                        |
| `[1]`              | Single-element `list` ✔️                         |
| `deque([1])`       | ✔️ Correct – a list (iterable) is passed        |
| `deque(1)`         | ❌ Error – `int` is not iterable                 |
| `tuple([1, 2])`    | ✔️ Converts a list to a tuple                    |
| `list((1, 2))`     | ✔️ Converts a tuple to a list                    |
| `for i in 5:`      | ❌ Error – `int` is not iterable                |
| `for i in range(5):`| ✔️ `range` is iterable                         |

---
------------------------------------------------------------------------------------------
---

🔄 Mutable vs Immutable in Python

| Concept        | Mutable                            | Immutable                          |
|----------------|------------------------------------|------------------------------------|
| 🔧 Definition  | Can be changed after creation   | Cannot be changed once created     |
| 🧠 Stored as   | Same object in memory (in-place)   | New object is created when changed |
| 📍 Example     | `list`, `dict`, `set`, `bytearray` | `int`, `float`, `str`, `tuple`, `bool`, `NoneType` |
| 🧪 Use case    | Good for dynamic data structures    | Safer for fixed data, hashing keys |
| 🛠️ Can you modify it? | ✅ Yes, you can change elements | ❌ No, changing creates a new object |

---

🧪 Example: List (Mutable)
```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # ➜ [1, 2, 3, 4] (a has changed too!)
```
- Both `a` and `b` point to same list object in memory.

---

🧪 Example: Tuple (Immutable)
```python
a = (1, 2, 3)
b = a
b = b + (4,)
print(a)  # ➜ (1, 2, 3) (unchanged)
print(b)  # ➜ (1, 2, 3, 4) (new tuple)
```
- `b` became a new object, `a` remains the same.

---

🔍 How to Check Mutability?

| Data Type     | Mutable? | Notes                        |
|---------------|----------|------------------------------|
| `list`        | ✅ Yes   | You can `append`, `remove`, etc. |
| `dict`        | ✅ Yes   | You can add/remove keys       |
| `set`         | ✅ Yes   | You can add/remove items      |
| `tuple`       | ❌ No    | Cannot change elements        |
| `str`         | ❌ No    | Every change creates a new string |
| `int`, `float`| ❌ No    | Arithmetic makes new objects  |

---

⚠️ Why Does It Matter?

| Scenario               | Importance                                          |
|------------------------|-----------------------------------------------------|
| Function arguments     | Mutable types can be **changed inside functions**!  |
| Caching / hashing      | Only **immutable types** can be used as `dict` keys |
| Debugging bugs         | Mutable references can cause **unexpected changes** |
| Performance            | Immutable types are **faster & safer** in some cases|

---

🧠 Summary

| Data Type     | Mutable? | Iterable? |
|---------------|----------|-----------|
| `list`        | ✅        | ✅        |
| `dict`        | ✅        | ✅        |
| `set`         | ✅        | ✅        |
| `tuple`       | ❌        | ✅        |
| `str`         | ❌        | ✅        |
| `int`, `float`| ❌        | ❌        |

---

"""
