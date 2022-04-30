"""
https://leetcode.com/problems/cinema-seat-allocation/
"""


from collections import defaultdict


class Solution:
    def maxNumberOfFamilies(
        self,
        n: int,
        reservedSeats: list[list[int]]
    ) -> int:
        # Build seats.
        seats = defaultdict(int)
        for r, c in reservedSeats:
            seats[r] |= 1 << (c - 1)

        # Check groups.
        # A row with no reserved seat can have maximum 2 groups.
        cnt = (n - len(seats)) << 1
        l = int('0111100000', 2)
        r = int('0000011110', 2)
        m = int('0001111000', 2)
        for row in seats.values():
            group = 0
            group += (row & l) == 0
            group += (row & r) == 0
            group += (row & m) == 0 and group == 0
            cnt += group

        return cnt


print(Solution().maxNumberOfFamilies(3,
                                     [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]))
