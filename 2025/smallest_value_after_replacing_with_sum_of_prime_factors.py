"""
https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/description/
"""


class Solution:
    """
    Solution
    """

    def smallest_value(self, n: int) -> int:
        """
        smallest value
        """
        m = n
        s = 0
        while m % 2 == 0:
            s += 2
            m >>= 1

        for i in range(3, int(m ** 0.5) + 1, 2):
            while m % i == 0:
                s += i
                m //= i

        if m > 2:
            s += m

        if s == n:
            return s

        return self.smallest_value(s)


print(Solution().smallest_value(15))
