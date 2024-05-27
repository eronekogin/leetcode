"""
https://leetcode.com/problems/minimum-average-difference/description/
"""


from itertools import accumulate


class Solution:
    """
    Solution
    """

    def minimum_average_difference(self, nums: list[int]) -> int:
        """
        minimum average difference
        """
        n = len(nums)
        prefix_sums = [0] + list(accumulate(nums))
        min_diff = prefix_sums[-1] // n
        min_index = n - 1
        for i in range(n - 1):
            curr_diff = abs(
                prefix_sums[i + 1] // (i + 1) -
                (prefix_sums[-1] - prefix_sums[i + 1]) // (n - i - 1)
            )
            if curr_diff < min_diff:
                min_diff, min_index = curr_diff, i
            elif curr_diff == min_diff and i < min_index:
                min_index = i

        return min_index


print(Solution().minimum_average_difference([2, 5, 3, 9, 5, 3]))
