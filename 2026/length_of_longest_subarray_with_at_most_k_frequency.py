"""
https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/
"""


class Solution:
    """
    Solution
    """

    def max_subarray_length(self, nums: list[int], k: int) -> int:
        """
        max subarray length
        """
        cnt: dict[int, int] = {}
        start = 0
        max_len = 0
        for end, x in enumerate(nums):
            cnt[x] = cnt.get(x, 0) + 1

            while cnt[x] > k:
                cnt[nums[start]] -= 1
                start += 1

            max_len = max(max_len, end - start + 1)

        return max_len
