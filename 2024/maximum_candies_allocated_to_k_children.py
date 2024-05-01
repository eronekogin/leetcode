"""
https://leetcode.com/problems/maximum-candies-allocated-to-k-children/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_candies(self, candies: list[int], k: int) -> int:
        """
        maximum candies
        """
        def can_distribute(target: int) -> bool:
            remain_children = k
            for candy in candies:
                remain_children -= candy // target
                if remain_children <= 0:
                    break

            return remain_children <= 0

        total = sum(candies)
        if total < k:
            return 0

        rslt = 0
        l, r = 1, total // k
        while l <= r:
            m = l + ((r - l) >> 1)
            if can_distribute(m):
                rslt = m
                l = m + 1
            else:
                r = m - 1

        return rslt


print(Solution().maximum_candies([5, 8, 6], 3))
