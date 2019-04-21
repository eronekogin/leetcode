"""
https://leetcode.com/problems/valid-sudoku/
"""

from typing import List


class Solution:
    def is_valid_sudoku(self, board: List[List[str]]) -> bool:
        refDict, totalLen = {}, len(board)
        for row in range(totalLen):
            for col in range(totalLen):
                c = board[row][col]
                if c == '.':
                    continue

                key1 = 'number-{}-row-{}'.format(c, row)
                key2 = 'number-{}-col-{}'.format(c, col)
                key3 = 'number-{}-blk-{}-{}'.format(
                    c, row // 3, col // 3)
                for key in [key1, key2, key3]:
                    refDict[key] = refDict.get(key, 0) + 1
                    if refDict[key] > 1:
                        return False

        return True


board = [
    [".", ".", ".", ".", "5", ".", ".", "1", "."],
    [".", "4", ".", "3", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "1"],
    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", "2", ".", "7", ".", ".", ".", "."],
    [".", "1", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", "2", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."]]

print(Solution().is_valid_sudoku(board))
