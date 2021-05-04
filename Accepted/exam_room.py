"""
https://leetcode.com/problems/exam-room/
"""

from bisect import insort_right


class ExamRoom:
    """
    1. Simply maintain a sorted list which contains the position where each
        previous student sat.
    2. For the next student, he should sit to the position where the distance
        between its adjancent students and the current student is maximum.
        2.1 We could then scan the sorted list from left to right, and check
            where is the maximum distance between two adjancent student sat
            previously. For example, for any adjancent student a and b, the
            distance is (b - a) // 2.
        2.2 We also need to check if the distance to the end of the list, which
            is N - 1 is greater than the current distance: if so, the next
            student could sit on the N - 1 th position.
    """

    def __init__(self, N: int):
        self.seats = []
        self.size = N

    def seat(self) -> int:
        N, L = self.size, self.seats
        if not L:
            rslt = 0
        else:
            d, rslt = L[0], 0
            for a, b in zip(L, L[1:]):
                if ((b - a) >> 1) > d:
                    d, rslt = (b - a) >> 1, (b + a) >> 1

            if N - 1 - L[-1] > d:
                rslt = N - 1

        insort_right(L, rslt)
        return rslt

    def leave(self, p: int) -> None:
        self.seats.remove(p)


e = ExamRoom(10)
e.seat()
e.seat()
e.seat()
e.seat()
e.leave(4)
e.seat()
