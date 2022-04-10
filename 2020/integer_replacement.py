"""
https://leetcode.com/problems/integer-replacement/
"""


class Solution:
    def integerReplacement(self, n: int) -> int:
        memo = {1: 0}  # number: minimum steps to reduce number to 1.

        def do(currNum: int):
            if currNum in memo:
                return memo[currNum]

            stepCnt = 0
            if currNum & 1:  # Odd number.
                stepCnt = 1 + min(do(currNum - 1), do(currNum + 1))
            else:
                stepCnt = 1 + do(currNum >> 1)

            memo[currNum] = stepCnt
            return stepCnt

        return do(n)

    def integerReplacement2(self, n: int) -> int:
        """
        In general we want to remove the 1 bits as many as possible when facing
        odd numbers. So we compare which brings more 1 bits between n - 1 and
        n + 1 by checking the last two bits of n:

        1. Case 0111:  n - 1 -> 0110, n + 1 -> 1000, so n + 1 is better.
        2. Case 0101:  n - 1 -> 0100, n + 1 -> 0110, so n - 1 is better.
        """
        currNum, stepCnt = n, 0
        while currNum > 1:
            if currNum & 1:  # Odd number.
                # Check which of currNum + 1 and currNum - 1 reduce more 1 bit
                # based on the last two bits of currNum.
                if currNum == 3 or not currNum & 2:  # Case 01.
                    # When currNum = 3, 11 -> 10 -> 1 takes less steps than
                    # 11 -> 100 -> 10 -> 1.
                    currNum -= 1
                else:
                    currNum += 1
            else:  # Even number.
                currNum >>= 1

            stepCnt += 1

        return stepCnt
