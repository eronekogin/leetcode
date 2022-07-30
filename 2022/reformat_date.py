"""
https://leetcode.com/problems/reformat-date/
"""


class Solution:
    def reformatDate(self, date: str) -> str:
        MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        day, month, year = date.split()
        return f'{year}-{(MONTHS.index(month) + 1):02d}-{(int(day[:-2])):02d}'
