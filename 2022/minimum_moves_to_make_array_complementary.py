"""
https://leetcode.com/problems/minimum-moves-to-make-array-complementary/
"""


class Solution:
    def minMoves(self, nums: list[int], limit: int) -> int:
        N = len(nums)

        # Build memo.
        memo = [0] * ((limit << 1) + 2)
        for i in range(N >> 1):
            l, r = nums[i], nums[N - 1 - i]
            memo[min(l, r) + 1] -= 1  # min one move
            memo[l + r] -= 1  # no move
            memo[l + r + 1] += 1  # max one move
            memo[max(l, r) + limit + 1] += 1  # max two moves

        # Calculate minimum moves.
        minMoves = float('inf')
        currMoves = len(nums)
        for i in range(2, (limit << 1) + 1):
            currMoves += memo[i]
            minMoves = min(minMoves, currMoves)

        return minMoves
