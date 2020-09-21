"""
https://leetcode.com/problems/car-pooling/
"""


from typing import List
from itertools import accumulate


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        General solution without knowing the range of the start and end
        locations.
        """
        memo = {}
        for p, s, e in trips:
            memo[s] = memo.get(s, 0) + p
            memo[e] = memo.get(e, 0) - p

        takenSeats = 0
        for k in sorted(memo.keys()):
            takenSeats += memo[k]
            if takenSeats > capacity:
                return False

        return True

    def carPooling2(self, trips: List[List[int]], capacity: int) -> bool:
        """
        Optimized by taking advantage of the start and end locations. The
        restriction in the question is [0, 1000], so we could use bucket sort
        to achieve O(n) instead of the general sort in python which is O(nlogn).
        """
        MAX_LOCATION = 1001
        memo = [0] * MAX_LOCATION
        for p, s, e in trips:
            memo[s] += p
            memo[e] -= p

        return all(x <= capacity for x in accumulate(memo))
