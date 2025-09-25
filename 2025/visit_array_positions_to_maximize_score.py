"""
https://leetcode.com/problems/visit-array-positions-to-maximize-score/description/
"""


class Solution:
    """
    Solution
    """

    def max_score(self, nums: list[int], x: int) -> int:
        """
        max score
        """
        prev_odd = prev_even = -x
        if nums[0] & 1:
            prev_odd = nums[0]
        else:
            prev_even = nums[0]

        for i in range(1, len(nums)):
            if nums[i] & 1:
                prev_odd = max(prev_odd, prev_even - x) + nums[i]
            else:
                prev_even = max(prev_even, prev_odd - x) + nums[i]

        return max(prev_odd, prev_even)


print(Solution().max_score([2, 3, 6, 1, 9, 2], 5))
