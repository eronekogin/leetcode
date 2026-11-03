"""
https://leetcode.com/problems/convert-date-to-binary/description/
"""


class Solution:
    """
    Solution
    """
    def convert_date_to_binary(self, date: str) -> str:
        """
        convert date to binary
        """
        [year, month, day] = date.split('-')

        return '-'.join([
            bin(int(year))[2:],
            bin(int(month))[2:],
            bin(int(day))[2:]
        ])
