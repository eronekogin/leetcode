"""
https://leetcode.com/problems/maximize-the-minimum-powered-city/description/
"""


class Solution:
    """
    Solution
    """

    def max_power(self, stations: list[int], r: int, k: int) -> int:
        """
        max power
        """
        def is_good(min_power_required, additional_stations):
            window_power = sum(stations[:r])
            additions = [0] * n
            for i in range(n):
                if i + r < n:
                    window_power += stations[i + r]

                if window_power < min_power_required:
                    needed = min_power_required - window_power
                    if needed > additional_stations:
                        return False

                    additions[min(n - 1, i + r)] += needed
                    window_power = min_power_required
                    additional_stations -= needed

                if i - r >= 0:
                    window_power -= stations[i - r] + additions[i - r]

            return True

        left = 0
        right = sum(stations) + k
        ans = 0
        n = len(stations)
        while left <= right:
            mid = (left + right) // 2
            if is_good(mid, k):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
