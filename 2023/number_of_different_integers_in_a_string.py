"""
https://leetcode.com/problems/number-of-different-integers-in-a-string/
"""


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        chars = [x if x.isdigit() else ' ' for x in word]
        return len(set(int(x) for x in ''.join(chars).split()))
