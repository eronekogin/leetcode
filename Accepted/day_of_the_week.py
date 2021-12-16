"""
https://leetcode.com/problems/day-of-the-week/
"""


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        def is_leap_year(year: int) -> bool:
            return (
                (year % 4 == 0 and year % 100 != 0)
                or (year % 100 == 0 and year % 400 == 0)
            )

        def days_since_start(day: int, month: int, year: int) -> int:
            days = 0
            for y in range(year - 1, BASE_YEAR, -1):
                days += 365 + is_leap_year(y)

            days += sum(NORMAL_MONTHS[:month - 1])
            days += day

            if month > 2:
                days += is_leap_year(year)

            return days

        BASE_YEAR = 1970
        DAYS_OF_WEEK = [
            "Thursday", "Friday", "Saturday", "Sunday",
            "Monday", "Tuesday", "Wednesday"
        ]
        NORMAL_MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        current = days_since_start(16, 12, 2021)
        target = days_since_start(day, month, year)
        return DAYS_OF_WEEK[(target - current) % 7]


print(Solution().dayOfTheWeek(31, 8, 2019))
