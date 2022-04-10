"""
https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
"""


from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """
        (t1 + t2) % 60 = 0 -> (t1 % 60 + t2 % 60) % 60 = 0 ->
        1. t1 % 60 = 0 and t2 % 60 = 0
        2. t1 % 60 + t2 % 60 = 60.
        """
        remainders, pairs = [0] * 60, 0
        for t in time:
            t1 = t % 60
            if t1 == 0:
                pairs += remainders[0]
            else:
                pairs += remainders[60 - t1]

            remainders[t1] += 1

        return pairs
