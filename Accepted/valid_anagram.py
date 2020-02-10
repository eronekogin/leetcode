"""
https://leetcode.com/problems/valid-anagram/
"""


from typing import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
