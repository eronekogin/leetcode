"""
https://leetcode.com/problems/beautiful-arrangement/
"""


from typing import Set


class Solution:
    def countArrangement(self, N: int) -> int:
        """
        Simple back-tracking from the last digit to the first digit as
        generally speaking the smaller the index is, the higher the
        arranged number will fit in. For example, index 1 could simply fix
        any number while index N could only fit its divisors.
        """
        def check(currIdx: int, remainNums: Set[int]) -> int:
            if currIdx == 1:
                return 1

            nextIdx = currIdx - 1
            return sum(
                check(nextIdx, remainNums - {num})
                for num in remainNums
                if not currIdx % num or not num % currIdx)

        return check(N, set(range(1, N + 1)))


print(Solution().countArrangement(3))
