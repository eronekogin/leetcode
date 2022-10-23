"""
https://leetcode.com/problems/coordinate-with-maximum-network-quality/
"""


from math import pow, sqrt, floor


class Solution:
    def bestCoordinate(self, towers: list[list[int]], radius: int) -> list[int]:
        def calc_signal(x1: int, y1: int, x2: int, y2: int, q: int) -> int:
            d = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
            if d <= radius:
                return floor(q / (1 + d))
            else:
                return 0

        maxNetworkQuality = -1
        rslt = [0, 0]
        for x1 in range(51):
            for y1 in range(51):
                currNetworkQuality = sum(
                    calc_signal(x1, y1, x2, y2, q)
                    for x2, y2, q in towers
                )
                if currNetworkQuality > maxNetworkQuality:
                    maxNetworkQuality = currNetworkQuality
                    rslt = [x1, y1]

        return rslt


print(Solution().bestCoordinate([[1, 2, 5], [2, 1, 7], [3, 1, 9]], 2))
