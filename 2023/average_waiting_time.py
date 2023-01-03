"""
https://leetcode.com/problems/average-waiting-time/
"""


class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        totalWaitTime, readyTime = 0, None
        for arrivalTime, prepareTime in customers:
            if readyTime is None or readyTime < arrivalTime:
                readyTime = arrivalTime + prepareTime
                totalWaitTime += prepareTime
            else:
                readyTime += prepareTime
                totalWaitTime += readyTime - arrivalTime

        return totalWaitTime / len(customers)


print(Solution().averageWaitingTime(
    [[2, 3], [6, 3], [7, 5], [11, 3], [15, 2], [18, 1]]))
