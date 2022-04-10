"""
https://leetcode.com/problems/maximum-profit-in-job-scheduling/
"""


from bisect import bisect_right


class Solution:
    def jobScheduling(
        self,
        startTime: list[int],
        endTime: list[int],
        profit: list[int]
    ) -> int:
        """
        Sort the jobs by the end time, and suppose dp[i] stands for the maximum
        profit that could be make at time i. Then for each job starting at i,
        we could binary search in the previous dp to find its maximum profit,
        and check it with the current maximum profit which is stored at the
        end of the dp to determine if we need to run the current job or not.
        """
        jobs = sorted(zip(startTime, endTime, profit), key=lambda job: job[1])
        dp = [[0, 0]]  # At time 0 we have 0 profit.
        for s, e, p in jobs:
            i = bisect_right(dp, [s + 1]) - 1
            newProfit = dp[i][1] + p
            if newProfit > dp[-1][1]:
                dp.append([e, newProfit])

        return dp[-1][1]
