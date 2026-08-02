"""
https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_chairs(self, s: str) -> int:
        """
        minimum chairs
        """
        curr = total = 0
        for c in s:
            if c == 'E':
                curr += 1
                total = max(curr, total)
            else:
                curr -= 1

        return total
