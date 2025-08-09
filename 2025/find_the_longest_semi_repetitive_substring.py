"""
https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/description/
"""


class Solution:
    """
    Solution
    """

    def longest_semi_repetitive_substring(self, s: str) -> int:
        """
        longest semi repetitive substring
        """
        if len(s) <= 1:
            return len(s)

        start = 0
        previous = -1
        max_len = -1
        for end in range(1, len(s)):
            if s[end] == s[end - 1]:
                if previous < 0:
                    previous = end
                else:
                    max_len = max(max_len, end - start)
                    start = previous
                    previous = end

        return max(max_len, end - start + 1)


print(Solution().longest_semi_repetitive_substring('0001'))
