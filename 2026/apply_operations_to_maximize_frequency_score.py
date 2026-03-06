"""
https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/description/
"""


class Solution:
    """
    Solution
    """

    def max_frequency_score(self, nums: list[int], k: int) -> int:
        """
        max frequency score
        """
        nums.sort()
        start = 0
        for end, x in enumerate(nums):
            k -= x - nums[(start + end) >> 1]

            if k < 0:
                k += nums[(start + end + 1) >> 1] - nums[start]
                start += 1

        return end - start + 1
