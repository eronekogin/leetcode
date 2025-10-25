"""
https://leetcode.com/problems/find-the-longest-equal-subarray/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def longest_equal_subarray(self, nums: list[int], k: int) -> int:
        """
        longest equal subarray
        """
        max_freq = 0
        start = 0
        cnt = Counter()

        for end, x in enumerate(nums):
            cnt[x] += 1
            max_freq = max(max_freq, cnt[x])

            if end - start + 1 - max_freq > k:
                # too many elements to delete in the current window
                cnt[nums[start]] -= 1
                start += 1

        return max_freq
