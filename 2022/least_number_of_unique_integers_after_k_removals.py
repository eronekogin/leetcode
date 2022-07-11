"""
https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
"""


from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        freqs = sorted(Counter(arr).values())
        remainMoves = k
        for i, freq in enumerate(freqs):
            if freq <= remainMoves:
                remainMoves -= freq
            else:
                return len(freqs) - i

        return 0  # All numbers are removed.
