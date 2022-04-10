"""
https://leetcode.com/problems/consecutive-numbers-sum/
"""


class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        """
        Suppose N is the sum of a consecutive sequence with i as its first item
        and the total number of items are k, then we have:
            N = i + (i + 1) + ... + (i + k - 1) = (i + i + k - 1) * k // 2
                = (2i + k - 1) * k // 2

        So we have:
            i = (2N + k - k^2) / 2k

        Since all the numbers in the sequence are positive, which means i >= 1
        and i must be an integer, then we have:

        1. i >= 1: 2N + k - k^2 >= 2k => 2N >= k + k^2 => 2N >= k * (k + 1)
        2. i is an integer: 2N + k - k^2 % 2K == 0. 
        """
        n = N << 1
        cnt, totalLen = 0, 1
        while n >= totalLen * (totalLen + 1):
            if (n + totalLen * (1 - totalLen)) % (totalLen << 1) == 0:
                cnt += 1

            totalLen += 1

        return cnt


print(Solution().consecutiveNumbersSum(5))
