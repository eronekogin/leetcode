"""
https://leetcode.com/problems/number-of-subarrays-with-and-value-of-k/description/
"""


class Solution:
    """
    Solution
    """

    def count_subarrays(self, nums: list[int], k: int) -> int:
        """
        count subarrays
        """
        rslt = 0
        prev: dict[int, int] = {}

        for x in nums:
            if x & k != k:
                # x & k <= k, so if x & k != k, it means x
                # cannot be part of the candidate subarray,
                # so we simply clear the previous memo
                prev = {}
                continue

            # x itself can form a subarray
            curr = {x: 1}

            for val, cnt in prev.items():
                new_val = val & x
                curr[new_val] = curr.get(new_val, 0) + cnt

            rslt += curr.get(k, 0)
            prev = curr

        return rslt
