"""
https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/
"""


from collections import Counter


class Solution:
    """
    Solution.
    """

    def count_k_difference(self, nums: list[int], k: int) -> int:
        """
        count_k_difference
        """
        cnt = Counter(nums)
        return (sum(cnt[x + k] + cnt[x - k] for x in nums)) >> 1
