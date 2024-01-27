"""
https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/description/
"""


class Solution:
    """
    Solution
    """

    def check_string(self, s: str) -> bool:
        """
        check_string
        """
        has_b = False
        for c in s:
            if c == 'a':
                if has_b:
                    return False
            else:
                has_b = True

        return True
