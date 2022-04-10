"""
https://leetcode.com/problems/broken-calculator/
"""


class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        """
        If we reverse the process to initially display Y on the calculator and
        want to display back to X, we could either divide Y by 2 or add 1 to Y.
        1. If Y = 2k + 1, then (Y + 1) / 2 + 1 = k + 2 takes 3 steps, while
            (Y + 3) / 2 = (2k + 4) / 2 = k + 2 takes 4 steps. So adding 1 first
            is the optimized solution when Y is odd.
        2. If Y = 2k, then Y / 2 + 1 = k + 1 takes 2 steps, while
            (Y + 2) / 2 = k + 1 takes 3 steps. So dividing by 2 first is the
            optimized solution when Y is even. 
        """
        steps = 0
        while Y > X:
            steps += 1
            if Y & 1:
                Y += 1
            else:
                Y >>= 1

        return steps + X - Y


print(Solution().brokenCalc(1, 1000000000))
