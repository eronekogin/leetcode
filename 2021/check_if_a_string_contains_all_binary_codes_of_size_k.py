"""
https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
"""


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        """
        1. Simply check if the total number of unique sub strings with length
            k is 2^k.
        2. We could use rolling hash to check each sub string.
        """
        need = 1 << k
        got = [False] * need
        allOnes = need - 1
        hashVal = 0

        for i, c in enumerate(s):
            hashVal = ((hashVal << 1) & allOnes) | int(c)
            if i >= k - 1 and not got[hashVal]:
                got[hashVal] = True
                need -= 1
                if not need:
                    return True

        return False
