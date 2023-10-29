"""
https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/
"""


class Solution:
    """
    Solution
    """

    def place_word_in_crossword(self, board: list[list[str]], word: str) -> bool:
        """
        * Find word in column means to rotate the board and check the rows in the rotated board.
        * Find word right to left means to find a reversed word from left to right.
        """
        words = [word, word[::-1]]
        n = len(word)
        for row in board + list(zip(*board)):
            candidates = ''.join(row).split('#')
            for w in words:
                for candidate in candidates:
                    if (
                        len(candidate) == n and
                        all(
                            candidate[i] == w[i] or candidate[i] == ' '
                            for i in range(n)
                        )
                    ):
                        return True

        return False


print(Solution().place_word_in_crossword([[" ", " "], [" ", " "]], 'a'))
