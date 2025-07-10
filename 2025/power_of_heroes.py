"""
https://leetcode.com/problems/power-of-heroes/description/

See https://leetcode.com/problems/power-of-heroes/solutions/3520233/c-java-python-sort-and-enumerate-each-maximum-value/
for detail explanation
"""


class Solution:
    """
    Solution
    """

    def sum_of_power(self, nums: list[int]) -> int:
        """
        sum of power
        """
        rslt = 0
        curr_power = 0
        mod = 10 ** 9 + 7

        for x in sorted(nums):
            rslt = (rslt + (curr_power + x) * x * x) % mod
            curr_power = (curr_power * 2 + x) % mod

        return rslt
