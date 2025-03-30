"""
https://leetcode.com/problems/count-the-number-of-fair-pairs/description/
"""


from bisect import bisect_left, bisect_right


class Solution:
    """
    Solution
    """

    def count_fair_pairs(self, nums: list[int], lower: int, upper: int) -> int:
        """
        count fair pairs
        """
        nums.sort()
        pairs = 0
        for i, x in enumerate(nums):
            l = bisect_left(nums, lower - x, i + 1)
            r = bisect_right(nums, upper - x, i + 1)
            pairs += r - l

        return pairs


print(Solution().count_fair_pairs([0, 1, 7, 4, 4, 5], 3, 6))
