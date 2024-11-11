"""
https://leetcode.com/problems/number-of-valid-clock-times/description/
"""


class Solution:
    """
    Solution
    """

    def count_time(self, time: str) -> int:
        """
        count time
        """
        cnt = 1

        if time[0] == '?':
            if time[1] == '?':
                cnt = 24
            elif int(time[1]) >= 4:
                cnt = 2
            else:
                cnt = 3
        else:
            if time[1] == '?':
                if int(time[0]) < 2:
                    cnt *= 10
                else:
                    cnt *= 4

        if time[3] == '?':
            cnt *= 6

        if time[4] == '?':
            cnt *= 10

        return cnt
