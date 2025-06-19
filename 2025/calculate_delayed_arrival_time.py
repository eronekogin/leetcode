"""
https://leetcode.com/problems/calculate-delayed-arrival-time/description/
"""


class Solution:
    """
    Solution
    """

    def find_delayed_arrival_time(self, arrival_time: int, delayed_time: int) -> int:
        """
        find delayed arrival time
        """
        return (arrival_time + delayed_time) % 24
