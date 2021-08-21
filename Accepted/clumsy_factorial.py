"""
https://leetcode.com/problems/clumsy-factorial/
"""


class Solution:
    def clumsy(self, n: int) -> int:
        """
        1. Check (k + 2) * (k + 1) // k = (k^2 + 3k + 2) // k = k + 3 + 2 // k.
            Since we are doing floor division, then we have:
            (k + 2) * (k + 1) // k = k + 3 when k > 2.
        2. Now check the following sequence:
            (k*(k-1)/(k-2))+(k-3)-((k-4)*(k-5)/(k-6))+(k-7)-((k-8)*(k-9)/(k-10))
            = (k+1)+(k-3)-(k-3)+(k-7)-(k-7)
            = (k+1)
        3. Then take four numbers as a group and check total numbers N % 4:
            3.1 If zero number left:
                f(n) = (k+1)+...+5-4*3/2+1 = k+1
            3.2 If 1 number left:
                f(n) = (k+1)+...+6-5*4/3+2-1 = k+2
            3.3 If 2 numbers left:
                f(n) = (k+1)+...+7-6*5/4+3-2*1 = k+2
            3.4 If 3 numbers left:
                f(n) = (k+1)+...+8-7*6/5+4-3*2/1 = k-1
        """
        CASES = [
            # When N > 4:
            1, 2, 2, -1,
            # When N <= 4:
            1, 2, 6, 7
        ]
        if n <= 4:
            return CASES[n + 3]
        else:
            return n + CASES[n % 4]
