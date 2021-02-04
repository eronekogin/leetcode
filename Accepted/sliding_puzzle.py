"""
https://leetcode.com/problems/sliding-puzzle/
"""


class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        R, C, T = len(board), len(board[0]), '123450'
        currBoards = [''.join(
            str(v)
            for r, row in enumerate(board)
            for c, v in enumerate(row))]
        moves = 0
        visited = set()
        while currBoards:
            nextBoards = []
            for currBoard in currBoards:
                if currBoard == T:  # Found the minimum move.
                    return moves

                if currBoard not in visited:
                    visited.add(currBoard)
                    zeroIdx = currBoard.index('0')
                    r, c = divmod(zeroIdx, C)
                    for nr, nc in [
                            (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                        if 0 <= nr < R and 0 <= nc < C:
                            nextBoard = list(currBoard)
                            swapIdx = nr * C + nc
                            nextBoard[zeroIdx], nextBoard[swapIdx] = (
                                nextBoard[swapIdx], nextBoard[zeroIdx])
                            nextBoards.append(''.join(nextBoard))

            currBoards = nextBoards
            moves += 1

        return -1  # Not found.


print(Solution().slidingPuzzle([[4, 1, 2], [5, 0, 3]]))
