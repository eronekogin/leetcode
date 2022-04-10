"""
https://leetcode.com/problems/keyboard-row/
"""


from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1 = set('qwertyuiop')
        r2 = set('asdfghjkl')
        r3 = set('zxcvbnm')
        rslt = []
        for w in words:
            rw = set(w.lower())
            if rw <= r1 or rw <= r2 or rw <= r3:
                rslt.append(w)

        return rslt
