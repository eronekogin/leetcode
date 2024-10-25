"""
https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/description/
"""


class Solution:
    """
    Solution
    """

    def longest_subarray(self, nums: list[int]) -> int:
        """
        longest subarray
        """
        max_num = max(nums)
        cnt = 0
        rslt = 0
        for x in nums:
            if x == max_num:
                cnt += 1
                continue

            rslt = max(rslt, cnt)
            cnt = 0

        return max(rslt, cnt)
