"""
https://leetcode.com/problems/find-closest-number-to-zero/description/
"""


class Solution:
    """
    Solution
    """

    def find_closest_number(self, nums: list[int]) -> int:
        """
        find closest number
        """
        diff = 10 ** 6
        candidate = -diff
        for x in nums:
            curr_diff = abs(x)
            if curr_diff == diff and x > candidate:
                candidate = x
            elif curr_diff < diff:
                diff = curr_diff
                candidate = x

        return candidate


print(Solution().find_closest_number([2, -1, 1]))
