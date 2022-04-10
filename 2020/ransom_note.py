"""
https://leetcode.com/problems/ransom-note/
"""


from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1, c2 = Counter(ransomNote), Counter(magazine)
        for c in c1:
            if c1[c] > c2[c]:
                return False

        return True
