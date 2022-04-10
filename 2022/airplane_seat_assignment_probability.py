"""
https://leetcode.com/problems/airplane-seat-assignment-probability/
"""


class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        """
        Suppose f(n) is the probability that the nth person gets its own seat,
        then we have:
            f(1) = 1

            f(n) =
                1 / n  # 1st person picks his own seat
            +   1 / n * 0  # 1st person picks nth seat
            +   (n-2) / n * (  # 1st person picks seat from 2 to n - 1
                    1 / (n - 2) * f(n - 1)  # 1st person picks the 2nd seat.
                +   1 / (n - 2) * f(n - 2)  # 1st person picks the 3rd seat.
                ...
                +   1 / (n - 2) * f(2)  # 1st person picks the n - 1 seat.
            = 1 / n * (f(n - 1) + f(n - 2) + ... + f(2) + f(1))

        So f(2) = f(3) = ... = f(n) = 1 / 2
        """
        if n == 1:
            return 1.0

        return 1 / 2
