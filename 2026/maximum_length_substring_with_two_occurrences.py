"""
https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_length_substring(self, s: str) -> int:
        """
        maximum length substring
        """
        start = 0
        memo: dict[str, int] = {}
        rslt = 0

        for end, c in enumerate(s):
            if c not in memo:
                memo[c] = 0

            memo[c] += 1
            while memo[c] > 2:
                memo[s[start]] -= 1
                start += 1

            rslt = max(rslt, end - start + 1)

        return rslt


print(Solution().maximum_length_substring('eebadadbfa'))
