"""
https://leetcode.com/problems/count-days-without-meetings/description/
"""


class Solution:
    """
    Solution
    """

    def count_days(self, days: int, meetings: list[list[int]]) -> int:
        """
        count days
        """
        meetings.sort()
        cnt = meetings[0][0] - 1
        prev_end = meetings[0][1]
        for curr_start, curr_end in meetings:
            if prev_end >= curr_start:
                prev_end = max(prev_end, curr_end)
            else:
                cnt += curr_start - prev_end - 1
                prev_end = curr_end

        return cnt + days - prev_end


print(Solution().count_days(8, [[3, 4], [4, 8], [2, 5], [3, 8]]))
