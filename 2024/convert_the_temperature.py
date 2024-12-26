"""
https://leetcode.com/problems/convert-the-temperature/description/
"""


class Solution:
    """
    Solution
    """

    def convert_temperature(self, celsius: float) -> list[float]:
        """
        convert temperature
        """
        return [
            (celsius * 100 + 27315) / 100,
            (celsius * 1800 + 32000) / 1000
        ]
