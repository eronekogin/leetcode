"""
https://leetcode.com/problems/number-of-zero-filled-subarrays/description/
"""


class Solution:
    """
    Solution
    """

    def zero_filled_subarray(self, nums: list[int]) -> int:
        """
        zero filled subarray
        """
        start = end = 0
        n, cnt = len(nums), 0
        while end < n:
            if nums[end] == 0:
                start = end
                while end + 1 < n and nums[end + 1] == 0:
                    end += 1

                x = end - start + 1
                cnt += (x * (x + 1)) >> 1

            end += 1

        return cnt


print(Solution().zero_filled_subarray([1, 3, 0, 0, 2, 0, 0, 4]))
