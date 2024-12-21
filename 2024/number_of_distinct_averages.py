"""
https://leetcode.com/problems/number-of-distinct-averages/description/
"""


class Solution:
    """
    Solution
    """

    def distinct_averages(self, nums: list[int]) -> int:
        """
        distinct averages
        """
        memo: set[float] = set()
        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            memo.add((nums[l] + nums[r]) / 2)
            l += 1
            r -= 1

        return len(memo)


print(Solution().distinct_averages([4, 1, 4, 0, 3, 5]))
