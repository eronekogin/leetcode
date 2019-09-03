"""
https://leetcode.com/problems/word-search/
"""

from typing import List, Set


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Using DFS solution with iterative method.
        """
        if not board or not board[0]:  # Board is empty.
            return False

        m, n, w = len(board), len(board[0]), len(word)
        if w > m * n:  # Word is too big.
            return False

        startIndexes = [
            (r, c) for r in range(m) for c in range(n) if board[r][c] == word[0]
        ]
        for r, c in startIndexes:
            visited = set()
            stack = [(r, c, 0, False)]
            while stack:
                cr, cc, i, backTrack = stack.pop()
                if backTrack:
                    visited.remove((cr, cc))
                    continue

                if i == w - 1:  # Matched all chars in the word.
                    return True

                visited.add((cr, cc))
                stack.append((cr, cc, i, True))  # Add backtrack node.

                # Try to match the next char in the word.
                ni = i + 1
                for nr, nc in self.get_neighbours(cr, cc, m, n):
                    if (nr, nc) not in visited and board[nr][nc] == word[ni]:
                        stack.append((nr, nc, ni, False))

        return False

    def get_neighbours(self, r: int, c: int, m: int, n: int) -> List[tuple]:
        rslt = []
        if r > 0:
            rslt.append((r - 1, c))

        if r < m - 1:
            rslt.append((r + 1, c))

        if c > 0:
            rslt.append((r, c - 1))

        if c < n - 1:
            rslt.append((r, c + 1))

        return rslt

    def exist2(self, board: List[List[str]], word: str) -> bool:
        """
        Using DFS solution with recurrsive method.
        """
        def chk_next_letter(r: int, c: int, i: int) -> bool:
            if i == w:
                return True

            if r < 0 or r == m or c < 0 or c == n or (
                    r, c) in visited or board[r][c] != word[i]:
                return False

            visited.add((r, c))
            rslt = chk_next_letter(r - 1, c, i + 1) or chk_next_letter(
                r + 1, c, i + 1) or chk_next_letter(
                    r, c - 1, i + 1) or chk_next_letter(r, c + 1, i + 1)
            visited.remove((r, c))
            return rslt

        if not board or not board[0]:  # Board is empty.
            return False

        m, n, w = len(board), len(board[0]), len(word)
        if w > m * n:  # Word is too big.
            return False

        visited = set()
        for r in range(m):
            for c in range(n):
                if chk_next_letter(r, c, 0):
                    return True

        return False


board = [["a", "a", "b", "b"], ["a", "a", "b", "b"]]
word = 'baa'
print(Solution().exist2(board, word))
