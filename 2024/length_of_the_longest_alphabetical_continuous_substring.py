"""
https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/description/
"""


class Solution:
    """
    Solution
    """

    def longest_continuous_substring(self, s: str) -> int:
        """
        longest continuous substring
        """
        start = 0
        max_len = 1
        for end in range(1, len(s)):
            if ord(s[end]) - ord(s[end - 1]) != 1:
                max_len = max(max_len, end - start)
                start = end

        return max(max_len, len(s) - start)
