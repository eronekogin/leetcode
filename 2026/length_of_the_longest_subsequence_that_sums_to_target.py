"""
https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def length_of_longest_subsequence(self, nums: list[int], target: int) -> int:
        """
        Docstring for length_of_longest_subsequence

        :param self: Description
        :param nums: Description
        :type nums: list[int]
        :param target: Description
        :type target: int
        :return: Description
        :rtype: int
        """
        dp = [0] + [-1] * target
        for x in nums:
            for curr_sum in reversed(range(x, target + 1)):
                if dp[curr_sum - x] + 1 > 0:
                    dp[curr_sum] = max(
                        dp[curr_sum],  # don't take x
                        dp[curr_sum - x] + 1  # take x
                    )

        return dp[-1]
