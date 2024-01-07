"""
https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/
"""


class Solution:
    """
    Solution
    """

    def max_sub_sequence(self, nums: list[int], k: int) -> list[int]:
        """
        max_sub_sequence
        """
        candidates = sorted((v, i) for i, v in enumerate(nums))[-k:]
        candidates.sort(key=lambda x: x[1])
        return [v for v, _ in candidates]


print(Solution().max_sub_sequence([2, 1, 3, 3], 2))
