"""
https://leetcode.com/problems/jewels-and-stones/
"""


from collections import Counter


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        cs = Counter(S)
        rslt = 0
        for c in J:
            rslt += cs[c]

        return rslt
