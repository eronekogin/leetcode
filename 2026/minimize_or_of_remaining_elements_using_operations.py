"""
https://leetcode.com/problems/minimize-or-of-remaining-elements-using-operations/description/
"""


class Solution:
    """
    Solution
    """

    def min_or_after_operations(self, nums: list[int], k: int) -> int:
        """
        min or after operations
        """
        mask = 0
        for bit in range(29, -1, -1):
            mask |= 1 << bit

            ops_needed = 0
            and_result = 0

            for x in nums:
                if and_result != 0:
                    and_result &= x
                    ops_needed += 1
                elif x & mask != 0:
                    and_result = x & mask

            if and_result != 0:
                ops_needed += 1

            if ops_needed > k:
                mask -= 1 << bit

        # Revert mask to get all result
        return (1 << 30) - 1 - mask
