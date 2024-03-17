"""
https://leetcode.com/problems/minimum-time-to-complete-trips/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_time(self, time: list[int], total_trips: int) -> int:
        """
        minimum time
        """
        l = min(time)
        r = total_trips * l + 1

        while l < r:
            m = l + ((r - l) >> 1)
            trips = sum(m // x for x in time)

            if trips >= total_trips:
                r = m
            else:
                l = m + 1

        return l


print(Solution().minimum_time([1, 2, 3], 5))
