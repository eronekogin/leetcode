"""
https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/description/
"""


class Solution:
    """
    Solution
    """

    def divide_string(self, s: str, k: int, fill: str) -> list[str]:
        """
        divide string
        """
        rslt: list[str] = []
        n = len(s)
        for i in range(0, n, k):
            if i + k <= n:
                rslt.append(s[i: i + k])
            else:
                rslt.append(s[i:] + fill * (k - (n - i)))

        return rslt
