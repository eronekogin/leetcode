"""
https://leetcode.com/problems/first-bad-version/
"""


class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Use binary search to reduce the times of calling of isBadVersion api.
        """
        def isBadVersion(t: int) -> bool:
            return t >= 1702766719

        l, r = 1, n + 1
        while l < r:
            m = l + ((r - l) >> 1)  # = (l + r) // 2, prevent overflow.
            if isBadVersion(m):
                r = m
            else:
                l = m + 1

        return l


print(Solution().firstBadVersion(2126753390))
