"""
https://leetcode.com/problems/minimum-time-to-finish-the-race/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_finish_time(self, tires: list[list[int]], change_time: int, num_laps: int) -> int:
        """
        minimum finish time
        """
        max_time = 10 ** 9
        dp: list[int] = [max_time] * (num_laps + 1)

        # Calculate the minimum time we need to complete the first i laps
        # without changing any tire.
        for f, r in tires:
            lap_time = total_time = f
            for i in range(1, num_laps + 1):
                dp[i] = min(dp[i], total_time)
                lap_time *= r
                total_time += lap_time
                if total_time > max_time:
                    break

        # Then use dp to determine whether we need to change the tire in the middle or not.
        for i in range(2, num_laps + 1):
            for j in range(1, i):
                dp[i] = min(dp[i], dp[j] + change_time + dp[i - j])

        return dp[num_laps]
