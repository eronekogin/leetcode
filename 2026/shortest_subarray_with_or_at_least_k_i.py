"""
https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_subarray_length(self, nums: list[int], k: int) -> int:
        """
        minimum subarray length
        """
        def add_to_cnt(curr_or: int, x: int) -> int:
            for i, y in enumerate(cnt):
                if x & (1 << i):
                    cnt[i] = y + 1

            return curr_or | x

        def remove_from_cnt(curr_or: int, x: int) -> int:
            for i, y in enumerate(cnt):
                if x & (1 << i):
                    cnt[i] = y - 1
                    if cnt[i] == 0:
                        curr_or &= ~(1 << i)

            return curr_or

        min_len = len(nums) + 1
        cnt = [0] * 32

        curr_or = 0
        start = 0
        for end, x in enumerate(nums):
            curr_or = add_to_cnt(curr_or, x)

            # reduce window size
            while start <= end and curr_or >= k:
                min_len = min(min_len, end - start + 1)
                curr_or = remove_from_cnt(curr_or, nums[start])
                start += 1

        if min_len == len(nums) + 1:
            return -1

        return min_len
