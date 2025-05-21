"""
https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/description/
"""


class Solution:
    """
    Solution
    """

    def minimize_max(self, nums: list[int], p: int) -> int:
        """
        minimize max
        """
        def calc_pairs(x: int) -> int:
            i = pairs = 0

            while i < n - 1:
                if nums[i + 1] - nums[i] <= x:
                    pairs += 1
                    i += 1

                i += 1

            return pairs

        nums.sort()
        n = len(nums)
        l, r = 0, nums[-1] - nums[0]
        while l < r:
            m = l + ((r - l) >> 1)
            if calc_pairs(m) >= p:
                r = m
            else:
                l = m + 1

        return l
