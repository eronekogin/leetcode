"""
https://leetcode.com/problems/length-of-last-word/
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])


s = 'Hello World'
print(Solution().lengthOfLastWord(s))
