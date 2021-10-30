"""
https://leetcode.com/problems/corporate-flight-bookings/
"""


class Solution:
    def corpFlightBookings(
        self,
        bookings: list[list[int]],
        n: int
    ) -> list[int]:
        """
        1. For each i, j, k in bookings, we need k more seats starting on
            the ith day and we don't need those seats starting on the j + 1 th
            day.
        2. Then we could simply accumulate the results for each day.
        """
        rslt = [0] * (n + 1)
        for start, end, seats in bookings:
            rslt[start - 1] += seats
            rslt[end] -= seats

        for i in range(1, n):
            rslt[i] += rslt[i - 1]

        return rslt[:-1]
