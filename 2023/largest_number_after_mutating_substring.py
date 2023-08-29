"""
https://leetcode.com/problems/largest-number-after-mutating-substring/
"""


class Solution:
    def maximumNumber(self, num: str, change: list[int]) -> str:
        chars = list(num)
        isChanged = False
        for i, c in enumerate(chars):
            x = int(c)
            if x < change[x]:
                chars[i] = str(change[x])
                isChanged = True
            elif isChanged and x > change[x]:
                break
        
        return ''.join(chars)
