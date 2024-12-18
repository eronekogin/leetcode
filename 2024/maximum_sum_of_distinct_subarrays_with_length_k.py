"""
https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_subarray_sum(self, nums: list[int], k: int) -> int:
        """
        maximum subarray sum
        """
        cnt: dict[int, int] = {}
        curr_sum = max_sum = 0

        for i, x in enumerate(nums):
            if i < k:
                cnt[x] = cnt.get(x, 0) + 1
                curr_sum += x
                continue

            if len(cnt) == k:
                max_sum = max(curr_sum, max_sum)

            curr_sum += x - nums[i - k]
            cnt[nums[i - k]] -= 1
            if cnt[nums[i - k]] == 0:
                del cnt[nums[i - k]]

            cnt[x] = cnt.get(x, 0) + 1

        if len(cnt) == k:
            max_sum = max(curr_sum, max_sum)

        return max_sum
