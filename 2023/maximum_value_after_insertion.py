"""
https://leetcode.com/problems/maximum-value-after-insertion/
"""


class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0] == '-':
            for i, c in enumerate(n):
                if c == '-':
                    continue

                if int(c) > x:
                    return n[:i] + str(x) + n[i:]
        else:
            for i, c in enumerate(n):
                if int(c) < x:
                    return n[:i] + str(x) + n[i:]
            
        return n + str(x)
    

print(Solution().maxValue('99', 9))