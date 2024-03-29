"""
https://leetcode.com/problems/number-of-days-between-two-dates/
"""


from datetime import date


class Solution:

    def daysBetweenDates(self, date1: str, date2: str) -> int:
        return abs((date.fromisoformat(date1) - date.fromisoformat(date2)).days)
