"""
https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
"""


class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        er, ec = entrance
        visited = {(er, ec)}
        queue: list[tuple[int, int, int]] = [(0, er, ec)]
        R, C = len(maze), len(maze[0])

        for currSteps, r, c in queue:
            if (r == 0 or r == R - 1 or c == 0 or c == C - 1) and not (r == er and c == ec):
                return currSteps
            else:
                for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited and maze[nr][nc] == '.':
                        visited.add((nr, nc))
                        queue.append((currSteps + 1, nr, nc))
        
        return -1


print(Solution().nearestExit([["+","+","+"],[".",".","."],["+","+","+"]], [1, 0]))