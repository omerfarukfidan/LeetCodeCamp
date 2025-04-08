"""
https://neetcode.io/problems/longest-substring-without-duplicates

Longest Substring Without Repeating Characters
Solved
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "zxyzxyz"

Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:

Input: s = "xxxx"

Output: 1
Constraints:

0 <= s.length <= 1000
s may consist of printable ASCII characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = []

        left, right = 0, 1
        ret = 0
        if s == " " or len(s) == 1:
            return 1
        while right < len(s):
            if len(sub) == 0 and s[left] != s[right]:
                sub.append(s[left])
                sub.append(s[right])
                right += 1
            elif s[right] not in sub:
                sub.append(s[right])
                right += 1
            else:
                sub = []
                left += 1
                right = left + 1
            ret = max(ret, len(sub))

        return ret

"""
Time Complexity:
The algorithm uses a two-pointer technique with a sliding window approach. The outer loop iterates through the string using the `right` pointer, while the `left` pointer adjusts to ensure that the substring remains valid (i.e., contains no repeating characters). In the worst case, each character is processed at most twice (once by the `right` pointer and once by the `left` pointer). Therefore, the time complexity is O(n), where n is the length of the input string `s`.

Space Complexity:
The space complexity is determined by the additional space used to store the substring `sub`. In the worst case, if all characters in the string are unique, the size of `sub` can grow to O(min(n, m)), where n is the length of the string and m is the size of the character set (e.g., 26 for lowercase letters, 128 for ASCII characters). However, since the substring can only contain unique characters, the space complexity can be considered O(min(n, m)) in the worst case. 

Overall, the algorithm is efficient with a linear time complexity and a space complexity that depends on the character set used.
"""
