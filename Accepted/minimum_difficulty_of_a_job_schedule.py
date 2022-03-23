"""
https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
"""


class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        def dfs(start: int, remainingDays: int) -> int:
            if (start, remainingDays) not in memo:
                if remainingDays == 1:  # Only one day left, doing all the job.
                    rslt = max(jobDifficulty[start:])
                else:
                    rslt, maxDifficulty = float('inf'), 0
                    for end in range(start, N - remainingDays + 1):
                        maxDifficulty = max(maxDifficulty, jobDifficulty[end])
                        rslt = min(
                            rslt,
                            maxDifficulty + dfs(end + 1, remainingDays - 1)
                        )
                memo[(start, remainingDays)] = rslt

            return memo[((start, remainingDays))]

        N = len(jobDifficulty)

        if N < d:  # Not enough jobs.
            return -1

        if N == d:  # One task everyday.
            return sum(jobDifficulty)

        memo = {}
        return dfs(0, d)


print(Solution().minDifficulty([1, 2, 3, 4, 5, 6], 2))
