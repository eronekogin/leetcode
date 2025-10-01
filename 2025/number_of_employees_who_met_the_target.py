"""
https://leetcode.com/problems/number-of-employees-who-met-the-target/description/
"""


class Solution:
    """
    Solution
    """

    def number_of_employees_who_met_target(self, hours: list[int], target: int) -> int:
        """
        number of employee who met target
        """
        return sum(x >= target for x in hours)
