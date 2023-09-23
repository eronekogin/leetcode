"""
https://leetcode.com/problems/last-day-where-you-can-still-cross/
"""


from collections import deque


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        def can_walk_from_top_to_bottom(lastDay: int):
            # Build matrix first.
            matrix = [[0] * col for _ in range(row)]
            for i in range(lastDay):
                r, c = cells[i]
                matrix[r - 1][c - 1] = 1

            queue = deque()
            
            # Inialize queue with all lands cells on the top row.
            for c in range(col):
                if matrix[0][c] == 0:
                    queue.append((0, c))
                    matrix[0][c] = 1  # Mark this cell as visited.

            while queue:
                r, c = queue.popleft()
                if r == bottomRow:
                    return True
                
                for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= nr < row and 0 <= nc < col and matrix[nr][nc] == 0:
                        matrix[nr][nc] = 1  # Mark this cell as visited.
                        queue.append((nr, nc))
            
            return False

        
        l, r = 1, len(cells)
        bottomRow = row - 1

        # Binary search to find the last day.
        while l < r:
            m = l + ((r - l) >> 1)
            if can_walk_from_top_to_bottom(m):
                l = m + 1
            else:
                r = m
        
        return l - 1
    

print(Solution().latestDayToCross(2, 2, [[1,1],[2,1],[1,2],[2,2]]))