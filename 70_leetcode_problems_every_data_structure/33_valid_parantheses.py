"""
https://leetcode.com/problems/valid-parentheses/description/

20. Valid Parentheses
Easy
Topics
Companies
Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true



Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
# MY SOLUTION

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        if len(s) == 1:
            return False

        for character in s:
            if not stack and character in (")","]","}"):
                return False
            if character in ("(", "[", "{"):
                stack.append(character)
            elif character == ")" and stack[-1] == "(":
                stack.pop()
            elif character == "]" and stack[-1] == "[":
                stack.pop()
            elif character == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        return False

# VIDEO SOLUTION WITH HASHMAP
class Solution:
    def isValid(self, s: str) -> bool:

        hashmap = {')':'(', ']':'[','}':'{' }

        stack = []

        for element in s:
            if stack and element in hashmap and hashmap[element] == stack[-1]:
                stack.pop()
            else:
                stack.append(element)

        return not stack    
