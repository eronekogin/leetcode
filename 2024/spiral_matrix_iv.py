"""
https://leetcode.com/problems/spiral-matrix-iv/description/
"""


from test_helper import ListNode


class Solution:
    """
    Solution
    """

    def spiral_matrix(self, m: int, n: int, head: ListNode) -> list[list[int]]:
        """
        spiral matrix
        """
        matrix: list[list[int]] = [[-1] * n for _ in range(m)]
        node = head
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        r = c = 0

        while node:
            matrix[r][c] = node.val
            dr, dc = directions[d]

            if (
                r + dr >= m or
                r + dc < 0 or
                c + dc >= n or
                c + dc < 0 or
                matrix[r + dr][c + dc] != -1
            ):
                d = (d + 1) % 4
                dr, dc = directions[d]

            r += dr
            c += dc
            node = node.next

        return matrix
