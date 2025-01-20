"""
https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_value(self, strs: list[str]) -> int:
        """
        maximum value
        """
        def get_value(s: str) -> int:
            v = 0
            for c in s:
                if c.isdigit():
                    v = v * 10 + int(c)
                else:
                    return len(s)

            return v

        return max(get_value(s) for s in strs)
