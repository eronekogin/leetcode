"""
https://leetcode.com/problems/count-square-sum-triples/
"""


from math import sqrt


class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        for a in range(1, n):
            for b in range(a + 1, n):
                c = sqrt(a * a + b * b)
                if int(c) == c and c <= n:
                    cnt += 2
        
        return cnt