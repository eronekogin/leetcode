"""
https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/
"""


class Solution:
    def minimumTimeRequired(self, jobs: list[int], k: int) -> int:
        def dfs(i: int):
            if i == N:  # All workers are assigned.
                return True

            for j in range(k):
                if capacity[j] >= sortedJobs[i]:
                    capacity[j] -= sortedJobs[i]
                    if dfs(i + 1):
                        return True

                    capacity[j] += sortedJobs[i]

                if capacity[j] == m:  # No more jobs to assign.
                    break

            return False

        N = len(jobs)
        sortedJobs = sorted(jobs, reverse=True)
        l, r = sortedJobs[0], sum(jobs)
        while l < r:
            m = l + ((r - l) >> 1)
            capacity = [m] * k
            if dfs(0):
                r = m
            else:
                l = m + 1

        return l
