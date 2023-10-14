"""
https://leetcode.com/problems/first-day-where-you-have-been-in-all-the-rooms/
"""


class Solution:
    """
    Solution
    """

    def first_day_been_in_all_rooms(self, next_visit: list[int]) -> int:
        """
        first_day_been_in_all_rooms
        """
        n = len(next_visit)
        mod = 10 ** 9 + 7

        # dp[i] stands for number of days to reach
        # the ith room starting from room zero.
        dp = [0] * n

        for i in range(1, n):
            # In order to reach room i, we have to reach room i - 1 first.
            # The first time to reach room i - 1 takes dp[i - 1] days.
            # Then we are redirected to room next_visit[i - 1] with one day.
            # Then in order to reach room i - 1 again we need
            # dp[i - 1] - dp[next_visit[i - 1]] days.
            # And we need one more day to reach the ith room.
            dp[i] = (dp[i - 1] * 2 - dp[next_visit[i - 1]] + 2) % mod

        return dp[-1] % mod


print(Solution().first_day_been_in_all_rooms([0, 0]))
