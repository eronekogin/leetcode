"""
https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
"""


class Solution:
    """
    Solution.
    """

    def final_value_after_operations(self, operations: list[str]) -> int:
        """
        final_value_after_operations
        """
        rslt = 0
        for op in operations:
            if '--' in op:
                rslt -= 1
            else:
                rslt += 1

        return rslt
