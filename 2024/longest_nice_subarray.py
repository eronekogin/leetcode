"""
https://leetcode.com/problems/longest-nice-subarray/description/
"""


class Solution:
    """
    Solution
    """

    def longest_nice_subarray(self, nums: list[int]) -> int:
        """
        For elements in the nice subarray, each of them have no
        common bits, in other words, there is no two element having
        the same value on the same bit, so when we remove an element
        from a nice subarray, we need to neuturalize itself by
        using xor, as a^a = 0.
        """
        rslt = curr_and = start = 0

        for end, x in enumerate(nums):
            while curr_and & x:
                curr_and ^= nums[start]
                start += 1

            curr_and |= x
            rslt = max(rslt, end - start + 1)

        return rslt
