"""
https://leetcode.com/problems/most-profit-assigning-work/
"""


from bisect import bisect_right
from collections import Counter


class Solution:
    def maxProfitAssignment(
            self,
            difficulty: list[int],
            profit: list[int],
            worker: list[int]) -> int:
        difficulties, profits = zip(*sorted(zip(difficulty, profit)))
        maxProfits = list(profits)

        # Calculate the current maximum profit at index i.
        maxProfit = float('-inf')
        for i in range(len(maxProfits)):
            if maxProfit < maxProfits[i]:
                maxProfit = maxProfits[i]
            else:
                maxProfits[i] = maxProfit

        # Then collect the maximum profit for each worker.
        workerCnt = Counter(worker)
        rslt = 0
        for w in workerCnt:
            i = bisect_right(difficulties, w)
            if i > 0:  # The worker could take a job.
                rslt += maxProfits[i - 1] * workerCnt[w]

        return rslt


print(Solution().maxProfitAssignment(
    [13, 55, 67],
    [78, 93, 100],
    [98, 78, 89],
))
