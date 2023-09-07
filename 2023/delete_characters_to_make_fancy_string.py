"""
https://leetcode.com/problems/delete-characters-to-make-fancy-string/
"""


class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        
        chars = [s[0], s[1]]
        for i in range(2, len(s)):
            if not (s[i] == chars[-1] == chars[-2]):
                chars.append(s[i])
        
        return ''.join(chars)
        
        
