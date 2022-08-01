"""
https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/
"""


class Solution:
    def minDifference(self, nums: list[int]) -> int:
        if len(nums) < 5:
            return 0

        sortedNums = sorted(nums)

        # 4 cases:
        #  * remove 3 largest, a[-4] - a[0]
        #  * remove 2 largest and 1 smallest, a[-3] - a[1]
        #  * remove 1 largest and 2 smallest, a[-2] - a[2]
        #  * remove 3 smallest, a[-1] - a[3]
        return min(b - a for a, b in zip(sortedNums[:4], sortedNums[-4:]))
