"""
https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/
"""


class Solution:
    """
    Solution
    """

    def number_of_beams(self, bank: list[str]) -> int:
        """
        number of beams
        """
        # Find the first row having security devices.
        start: int | None = None
        for i, row in enumerate(bank):
            if row.find('1') >= 0:
                start = i
                break

        if start is None:
            return 0

        cnt = 0
        for end in range(start + 1, len(bank)):
            # No security device on the current row.
            if bank[end].find('1') == -1:
                continue

            cnt += bank[start].count('1') * bank[end].count('1')
            start = end

        return cnt
