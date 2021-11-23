"""
https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/
"""


class Solution:
    def movesToMakeZigzag(self, nums: list[int]) -> int:
        """
        Either make nums[odd] smaller or make nums[even] smaller.
        """
        moves = [0, 0]
        A = [float('inf')] + nums + [float('inf')]
        for i in range(1, len(A) - 1):
            moves[i & 1] += max(0, A[i] - min(A[i - 1], A[i + 1]) + 1)

        return min(moves)
