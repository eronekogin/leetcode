"""
https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/description/
"""


class Solution:
    """
    Solution
    """

    def convert_time(self, current: str, correct: str) -> int:
        """
        convert time
        """
        def convert_to_min(s: str) -> int:
            h, m = s.split(':')
            return int(h) * 60 + int(m)

        diff_min = convert_to_min(correct) - convert_to_min(current)
        rslt = 0

        for t in [60, 15, 5, 1]:
            q, diff_min = divmod(diff_min, t)
            rslt += q
            if diff_min == 0:
                break

        return rslt
