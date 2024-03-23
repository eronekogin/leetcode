"""
https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/description/
"""


class Solution:
    """
    Solution
    """

    def cells_in_range(self, s: str) -> list[str]:
        """
        cells in range
        """
        c1 = ord(s[0])
        r1 = int(s[1])
        c2 = ord(s[3])
        r2 = int(s[4])
        return [
            chr(c) + str(r)
            for c in range(c1, c2 + 1)
            for r in range(r1, r2 + 1)
        ]
