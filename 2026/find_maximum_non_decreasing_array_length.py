"""
https://leetcode.com/problems/find-maximum-non-decreasing-array-length/description/
"""


from bisect import bisect_left
from itertools import accumulate


class Solution:
    """
    Docstring for Solution
    """

    def find_maximum_length(self, nums: list[int]) -> int:
        """
        The sum of last group i...j-1 is ps[j] - ps[i],
        Suppose the next group is j...k-1, so
        ps[k] - ps[j] >= ps[j] - ps[i], which equals to
        ps[k] >= 2 * ps[j] - ps[i], and since ps array
        is non-decreasing, we could apply binary search to
        find the lowest index of such k to make the next
        group smallest, so that after applying the operation,
        the result array has the maximum length.
        """
        n = len(nums)
        prefix_sums = list(accumulate(nums, initial=0))
        prev = [0] * (n + 2)
        dp = [0] * (n + 1)
        start = 0

        for end in range(1, n + 1):
            start = max(start, prev[end])

            dp[end] = dp[start] + 1

            k = bisect_left(
                prefix_sums,
                prefix_sums[end] * 2 - prefix_sums[start]
            )

            prev[k] = end

        return dp[n]
