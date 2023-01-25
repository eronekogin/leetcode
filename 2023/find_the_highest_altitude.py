"""
https://leetcode.com/problems/find-the-highest-altitude/
"""


class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        maxSum = preSum = 0
        for num in gain:
            preSum += num
            maxSum = max(maxSum, preSum)

        return maxSum
