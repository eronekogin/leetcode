"""
https://leetcode.com/problems/house-robber-ii/
"""


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def line_rob(start: int, end: int) -> int:
            preMax = currMax = 0
            for i in range(start, end):
                preMax, currMax = currMax, max(preMax + nums[i], currMax)

            return currMax

        n = len(nums)
        if not n:
            return 0

        if n == 1:
            return nums[0]

        return max(line_rob(0, n - 1), line_rob(1, n))


print(Solution().rob([1, 3, 1, 3, 100]))
