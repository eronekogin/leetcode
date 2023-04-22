"""
https://leetcode.com/problems/determine-color-of-a-chessboard-square/
"""


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        NUMBER_OFFSET = 1
        CHAR_OFFSET = ord('a')
        charIndex = ord(coordinates[0]) - CHAR_OFFSET
        numberIndex = int(coordinates[1]) - NUMBER_OFFSET
        return (charIndex & 1) != (numberIndex & 1)
