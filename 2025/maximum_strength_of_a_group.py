"""
https://leetcode.com/problems/maximum-strength-of-a-group/description/
"""


from math import prod


class Solution:
    """
    Solution
    """

    def max_strength(self, nums: list[int]) -> int:
        """
        max strength
        """
        neg_nums, pos_nums = [], []
        has_zero = False
        for x in nums:
            if x < 0:
                neg_nums.append(x)
            elif x > 0:
                pos_nums.append(x)
            else:
                has_zero = True

        neg_nums.sort()
        if len(neg_nums) & 1:
            if len(neg_nums) > 1:
                neg_nums.pop()
            elif pos_nums:
                return prod(pos_nums)
            elif has_zero:
                return 0
            else:
                return neg_nums[-1]

        if not neg_nums and not pos_nums:
            return 0

        return prod(neg_nums) * prod(pos_nums)


print(Solution().max_strength([2, 2, 7, 0, -4, 9, 4]))
