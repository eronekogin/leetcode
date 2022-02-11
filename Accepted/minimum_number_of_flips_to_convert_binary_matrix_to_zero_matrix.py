"""
https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/
"""


class Solution:
    def minFlips(self, mat: list[list[int]]) -> int:
        """
        Since mat could have maximum 3 rows or columns, we could map each cell
        into one bit of an integer with length m * n. Then perform BFS and try
        to flip at each bit of the integer.
        """
        R, C = len(mat), len(mat[0])
        initNum = sum(
            v << (r * C + c)
            for r, row in enumerate(mat)
            for c, v in enumerate(row)
        )
        queue = [(initNum, 0)]
        visited = {initNum}
        for currNum, flipCnt in queue:
            if not currNum:  # The current number become 0.
                return flipCnt

            # Make one flip on every bit.
            for r in range(R):
                for c in range(C):
                    nextNum = currNum
                    for nr, nc in [(r, c), (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                        if 0 <= nr < R and 0 <= nc < C:
                            nextNum ^= 1 << (nr * C + nc)

                    if nextNum not in visited:
                        queue.append((nextNum, flipCnt + 1))
                        visited.add(nextNum)

        return -1  # Not found.
