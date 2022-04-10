"""
https://leetcode.com/problems/snakes-and-ladders/
"""


from collections import deque
from typing import Iterator


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        """
        Simple BFS. Notice that it is better to convert [1, N * N] to
        [0, N * N - 1] so that it could match the matrix easily.
        """
        def destinations(start: int) -> Iterator[tuple[int]]:
            for nextNum in range(start + 1, min(start + 7, GOAL)):
                r, c = divmod(nextNum, N)
                if r & 1:  # odd rows.
                    yield (nextNum, N - 1 - r, N - 1 - c)
                else:  # even rows.
                    yield (nextNum, N - 1 - r, c)

        N = len(board)
        GOAL = N * N
        queue = deque([(0, 0)])  # (currSteps, currNum)
        visited = {0}
        while queue:
            currSteps, currNum = queue.popleft()
            if currNum == GOAL - 1:
                return currSteps

            nextSteps = currSteps + 1
            for nextNum, nr, nc in destinations(currNum):
                if nextNum not in visited:
                    visited.add(nextNum)
                    if board[nr][nc] == -1:
                        queue.append((nextSteps, nextNum))
                    elif board[nr][nc] - 1 not in visited:
                        queue.append((nextSteps, board[nr][nc] - 1))

        return -1


print(Solution().snakesAndLadders([
    [-1, -1, 2, -1],
    [14, 2, 12, 3],
    [4, 9, 1, 11],
    [-1, 2, 1, 16]
]))
