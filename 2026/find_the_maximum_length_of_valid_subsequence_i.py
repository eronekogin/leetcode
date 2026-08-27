"""
https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_length(self, nums: list[int]) -> int:
        """
        maximum length
        """
        total_odd = len([x for x in nums if x & 1])

        # Even parity check
        rslt = max(total_odd, len(nums) - total_odd)

        # Odd parity check
        curr_parity = nums[0] & 1
        cnt = 0
        for x in nums:
            if x & 1 == curr_parity:
                cnt += 1
                curr_parity = 1 - curr_parity

        return max(rslt, cnt)
