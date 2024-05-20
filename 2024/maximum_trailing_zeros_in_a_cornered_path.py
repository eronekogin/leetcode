"""
https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/description/
"""


class Solution:
    """
    Solution
    """

    def max_trailing_zeros(self, grid: list[list[int]]) -> int:
        """
        max trailing zeros
        """
        def count_valid_factors(x: int) -> tuple[int, int]:
            f2 = f5 = 0
            while x % 2 == 0:
                f2 += 1
                x //= 2

            while x % 5 == 0:
                f5 += 1
                x //= 5

            return (f2, f5)

        m, n = len(grid), len(grid[0])
        left: list[list[tuple[int, int]]] = [
            [(0, 0) for _ in range(n)]
            for _ in range(m)
        ]
        top: list[list[tuple[int, int]]] = [
            [(0, 0) for _ in range(n)]
            for _ in range(m)
        ]
        factors: list[list[tuple[int, int]]] = [
            [count_valid_factors(v) for v in row]
            for row in grid
        ]

        for r in range(m):
            for c in range(n):
                f2, f5 = factors[r][c]
                if c == 0:
                    left[r][c] = (f2, f5)
                else:
                    left[r][c] = (
                        left[r][c - 1][0] + f2,
                        left[r][c - 1][1] + f5
                    )

        for c in range(n):
            for r in range(m):
                f2, f5 = factors[r][c]
                if r == 0:
                    top[r][c] = (f2, f5)
                else:
                    top[r][c] = (
                        top[r - 1][c][0] + f2,
                        top[r - 1][c][1] + f5
                    )

        max_zeros = 0
        for r in range(m):
            for c in range(n):
                f2, f5 = factors[r][c]
                a, b = top[m - 1][c]
                d, e = left[r][n - 1]
                a1, b1 = top[r][c]
                a2, b2 = left[r][c]

                # Top to left.
                curr = [a1 + a2 - f2, b1 + b2 - f5]
                max_zeros = max(max_zeros, min(curr))

                # Top to right.
                curr = [d - a2 + a1, e - b2 + b1]
                max_zeros = max(max_zeros, min(curr))

                # Bottom to left.
                curr = [a - a1 + a2, b - b1 + b2]
                max_zeros = max(max_zeros, min(curr))

                # Bottom to right.
                curr = [a - a1 + d - a2 + f2, b - b1 + e - b2 + f5]
                max_zeros = max(max_zeros, min(curr))

        return max_zeros
