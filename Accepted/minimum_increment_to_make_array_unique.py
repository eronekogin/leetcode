"""
https://leetcode.com/problems/minimum-increment-to-make-array-unique/
"""


class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        currMax, totalMoves = float('-inf'), 0
        for num in sorted(nums):
            if num < currMax:
                totalMoves += currMax - num
            else:
                currMax = num

            currMax += 1

        return totalMoves


print(Solution().minIncrementForUnique([1, 2, 2]))
