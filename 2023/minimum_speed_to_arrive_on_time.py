"""
https://leetcode.com/problems/minimum-speed-to-arrive-on-time/
"""


from math import ceil


class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        def calc_time(speed: int):
            total = sum(ceil(dist[i] / speed) for i in range(N))
            return total + dist[-1] / speed

        l, r, s = 1, 10 ** 7, -1
        N = len(dist) - 1
        while l <= r:
            m = l + ((r - l) >> 1)
            t = calc_time(m)
            if t > hour:
                l = m + 1
            else:
                r = m - 1
                s = m

        return s


print(Solution().minSpeedOnTime([1, 3, 2], 1.9))
