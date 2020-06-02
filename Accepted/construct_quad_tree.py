"""
https://leetcode.com/problems/construct-quad-tree/
"""


from typing import List
from test_helper import QuadTreeNode


class Solution:
    def construct(self, grid: List[List[int]]) -> QuadTreeNode:
        def chk_values(sr: int, sc: int, l: int) -> bool:
            uniqueItem = grid[sr][sc]
            for r in range(sr, sr + l):
                for c in range(sc, sc + l):
                    if grid[r][c] != uniqueItem:
                        return False

            return True

        def create_node(sr: int, sc: int, l: int) -> QuadTreeNode:
            if chk_values(sr, sc, l):  # The current grid is a leaf node.
                return QuadTreeNode(grid[sr][sc], 1, None, None, None, None)

            # The current node has to be a non-leaf node now.
            nl = l >> 1
            return QuadTreeNode(
                1,
                0,
                create_node(sr, sc, nl),
                create_node(sr, sc + nl, nl),
                create_node(sr + nl, sc, nl),
                create_node(sr + nl, sc + nl, nl))

        return create_node(0, 0, len(grid))


print(Solution().construct(
    [
        [0, 1],
        [1, 0]
    ]
))
