"""
https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def minimum_operations(self, nums: list[int]) -> int:
        """
        minimum operations
        """
        def pad(nums: list[tuple[int, int]]) -> list[tuple[int, int]]:
            return nums + [(-1, 0)] * (2 - len(nums))

        n = len(nums)
        if n <= 1:
            return 0

        even_candidates = pad(Counter(nums[::2]).most_common(2))
        odd_candidates = pad(Counter(nums[1::2]).most_common(2))

        if even_candidates[0][0] != odd_candidates[0][0]:
            return n - even_candidates[0][1] - odd_candidates[0][1]

        return n - max(
            even_candidates[0][1] + odd_candidates[1][1],
            even_candidates[1][1] + odd_candidates[0][1]
        )


print(Solution().minimum_operations([1, 2, 2, 2, 2]))
