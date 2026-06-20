"""
https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/description/
"""


class Solution:
    """
    Solution
    """

    def find_latest_time(self, s: str) -> str:
        """
        find latest time
        """
        rslt = list(s)
        if rslt[0] == '?':
            if rslt[1] in '?10':
                rslt[0] = '1'
            else:
                rslt[0] = '0'

        if rslt[1] == '?':
            if rslt[0] == '1':
                rslt[1] = '1'
            else:
                rslt[1] = '9'

        if rslt[3] == '?':
            rslt[3] = '5'

        if rslt[4] == '?':
            rslt[4] = '9'

        return ''.join(rslt)
