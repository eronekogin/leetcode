"""
https://leetcode.com/problems/determine-if-two-events-have-conflict/description/
"""


class Solution:
    """
    Solution
    """

    def have_conflict(self, event1: list[str], event2: list[str]) -> bool:
        """
        have conflict
        """
        def convert_time(s: str) -> int:
            h, m = s.split(':')
            return int(h) * 60 + int(m)

        s1 = convert_time(event1[0])
        e1 = convert_time(event1[1])
        s2 = convert_time(event2[0])
        e2 = convert_time(event2[1])

        if e1 < s2 or s1 > e2:
            return False

        return True
