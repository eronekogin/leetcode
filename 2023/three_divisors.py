"""
https://leetcode.com/problems/three-divisors/
"""


class Solution:
    def isThree(self, n: int) -> bool:
        divisorCnt = 0
        for i in range(1, int(n ** 0.5) + 1):
            q, r = divmod(n, i)
            if r == 0:
                divisorCnt += 1 + (i != q)
            
            if divisorCnt > 3:
                return False
            
        return divisorCnt == 3
            

print(Solution().isThree(12))