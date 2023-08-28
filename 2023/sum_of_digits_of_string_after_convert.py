"""
https://leetcode.com/problems/sum-of-digits-of-string-after-convert/
"""


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def digits_sum(x: int):
            rslt = 0
            while x:
                x, r = divmod(x, 10)
                rslt += r
            
            return rslt

        OFFSET = ord('a')
        currSum = 0
        for c in s:
            q, r = divmod(ord(c) - OFFSET + 1, 10)
            currSum += q + r
        
        for _ in range(k - 1):
            currSum = digits_sum(currSum)
        
        return currSum
