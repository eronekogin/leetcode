"""
https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/
"""


class Solution:
    def minMoves(self, nums: list[int], k: int) -> int:
        """
        1. Record positions of all ones as ones.

        2. Take the median position of a window with length k, then we have
            two steps to make the current window contains consecutive ones:
            2.1 move the median to the other places, which adds moves.
            2.2 move the median to the target consecutive indexes, which
                saves moves.

        3. See https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/solutions/987607/o-n-explanation-with-picture/?orderBy=most_votes
            for more expalanations.
        """
        ones = [i for i, num in enumerate(nums) if num == 1]
        N = len(ones)
        preSums: list[int] = [0]
        for v in ones:
            preSums.append(preSums[-1] + v)

        rslt = float('inf')

        if k & 1:
            r = (k - 1) >> 1
            for i in range(r, N - r):
                right = preSums[i + r + 1] - preSums[i + 1]
                left = preSums[i] - preSums[i - r]
                rslt = min(rslt, right - left)

            return rslt - r * (r + 1)
        else:
            r = (k - 2) >> 1
            for i in range(r, N - r - 1):
                right = preSums[i + r + 2] - preSums[i + 1]
                left = preSums[i] - preSums[i - r]
                rslt = min(rslt, right - left - ones[i])

            return rslt - r * (r + 1) - (r + 1)
