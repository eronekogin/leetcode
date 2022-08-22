"""
https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/
"""


class Solution:
    def minSwaps(self, grid: list[list[int]]) -> int:
        """
        Count the trailing zeros for each row first, then for each row, try
        to swap with the nearest row that satisfy the current row requirement.
        """
        def count_trailing_zeros(row: list[int]) -> int:
            cnt = 0
            for num in reversed(row):
                if num == 0:
                    cnt += 1
                else:
                    break

            return cnt

        N = len(grid)
        trailingZeros = [count_trailing_zeros(row) for row in grid]
        cnt = 0
        for i in range(N):
            minimumRequiredTrailingZeros = N - i - 1
            if trailingZeros[i] >= minimumRequiredTrailingZeros:
                # No need to swap on the current row.
                continue

            isSwapped = False
            for j in range(i + 1, N):
                if trailingZeros[j] >= minimumRequiredTrailingZeros:
                    cnt += j - i
                    trailingZeros[i + 1: j + 1] = trailingZeros[i: j]
                    isSwapped = True
                    break

            if not isSwapped:
                return -1

        return cnt
