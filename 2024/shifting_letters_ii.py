"""
https://leetcode.com/problems/shifting-letters-ii/description/
"""


class Solution:
    """
    Solution
    """

    def shifting_letters(self, s: str, shifts: list[list[int]]) -> str:
        """
        shifting letters
        """
        flags = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            flags[start] += 1 if direction == 1 else -1
            flags[end + 1] += -1 if direction == 1 else 1

        offset = 0
        base = ord('a')
        rslt = list(s)
        for i, c in enumerate(s):
            offset += flags[i]
            rslt[i] = chr(
                (ord(c) + offset - base) % 26 + base
            )

        return ''.join(rslt)


print(Solution().shifting_letters('abc', [[0, 1, 0], [1, 2, 1], [0, 2, 1]]))
