"""
https://leetcode.com/problems/interleaving-string/
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        We could expand each chars in s1 and s2 and form a board like below:

        s1 = aab, s2 = abc, s3 = aaabcb, then x stands for a possible path.

        x--a--x--b--o--c--o
        |     |     |     |
        a     a     a     a
        |     |     |     |
        o--a--x--b--o--c--o
        |     |     |     |
        a     a     a     a
        |     |     |     |
        o--a--x--b--x--c--x
        |     |     |     |
        b     b     b     b
        |     |     |     |
        o--a--o--b--o--c--x

        The the problem is turned into checking if there is a path from
        top-left to the bottom-right when following the instruction from chars
        in s3. Then we could apply DFS solution for it.
        """
        maxRow, maxCol, n = len(s1), len(s2), len(s3)
        if maxRow + maxCol != n:
            return False

        workStack, visited = [(0, 0)], {(0, 0)}
        while workStack:
            row, col = workStack.pop()
            if row + col == n:
                return True  # Found a possible path.

            np = (row + 1, col)
            if row < maxRow and s1[row] == s3[row + col] and np not in visited:
                workStack.append(np)
                visited.add(np)

            np = (row, col + 1)
            if col < maxCol and s2[col] == s3[row + col] and np not in visited:
                workStack.append(np)
                visited.add(np)

        return False  # Not found.
