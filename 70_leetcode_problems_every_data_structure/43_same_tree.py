"""
https://leetcode.com/problems/same-tree/description/
100. Same Tree
Easy
Topics
Companies
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.



Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false


Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""
# VIDEO SOLUTION

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        stack = [(p, q)]

        while stack:
            node1, node2 = stack.pop()

            if not node1 and not node2:
                continue
            elif None in [node1, node2] or node1.val != node2.val:
                return False

            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))

        return True


"""
✅ 1. `stack = [(p, q)]` neden parantezli, neden `stack = [p, q]` değil?

Bu fark, list of tuples ile list of elements arasındaki farktan kaynaklanıyor:

- `stack = [(p, q)]`  
  Bu bir liste içinde tek bir tuple barındırır.  
  Yani: `[(p, q)]` → liste: `[(p, q)]`  
  Bu sayede sen `stack.pop()` dediğinde bir seferde hem `p` hem de `q` gelir:
  ```python
  node1, node2 = stack.pop()  # bu şekilde unpack edebilirsin
  ```

- `stack = [p, q]`  
  Bu ise p ve q’yu sırayla listeye koyar, tuple değil.  
  Liste: `[p, q]`  
  Bu durumda `stack.pop()` sadece bir node döner (ya p ya da q), dolayısıyla:
  ```python
  node1, node2 = stack.pop()  # ❌ HATA! Çünkü tek değer geliyor, 2 değişkene atanamaz
  ```

📌 Özet: `[(p, q)]` yaparak "bu iki node birlikte kontrol edilecek" diyorsun. Bu ağaç karşılaştırmalarında yaygın bir tekniktir çünkü aynı pozisyondaki node’ları birlikte ele almak istersin.

---

✅ 2. `deque([root])` neden köşeli parantez içinde?

Bu da benzer bir durum. `deque()` fonksiyonu bir iterable alır, yani liste, tuple, string vs.

Eğer şöyle yazarsan:
```python
deque(root)  # ❌ yanlış!
```
Bu durumda `root` bir `TreeNode` nesnesi olduğu için Python `TypeError` verir çünkü `TreeNode` iterable değildir.

Ama şöyle yazarsan:
```python
deque([root])  # ✅ doğru!
```
Bu, root’u bir listeye sarar ve `deque`'ye bir iterable (liste) vermiş olursun. Bu durumda deque içeriği:
```python
deque([root])
```

Sonra `popleft()` ile node alırsın.

---

✅ 3. `deque([(root, 1)])` neden tuple içinde?

Bu da yine ilk sorunun cevabıyla bağlantılı.

```python
queue = deque([(root, 1)])
```

Burada her node ile beraber bulunduğu seviyeyi de saklamak istiyorsun. Yani:
- `root` → node
- `1` → seviyesi

Tuple halinde `(node, level)` şeklinde ekleniyor ki:
```python
node, level = queue.popleft()
```
şeklinde unpack edebilesin.

---

Kısa özet:

| Yazım             | Anlamı                                                      |
|-------------------|-------------------------------------------------------------|
| `[p, q]`          | Liste içinde 2 ayrı öğe: `p` ve `q`                          |
| `[(p, q)]`        | Liste içinde tek bir tuple: `(p, q)`                    |
| `deque([root])`   | Deque içinde tek bir öğe (root node)                        |
| `deque([(root, 1)])` | Deque içinde tek bir tuple: `(node, level)`              |

"""
