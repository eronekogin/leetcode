"""
https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/
"""


class Solution:
    """
    Solution
    """

    def are_numbers_ascending(self, s: str) -> bool:
        """
        are_numbers_ascending
        """
        prev = -1
        for w in s.split():
            if w.isnumeric():
                curr = int(w)
                if curr <= prev:
                    return False

                prev = curr

        return True
