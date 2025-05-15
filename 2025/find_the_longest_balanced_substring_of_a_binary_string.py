"""
https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/description/
"""


class Solution:
    """
    Solution
    """

    def find_the_longest_balanced_substring(self, s: str) -> int:
        """
        find the longest balanced substring
        """
        zeros = ones = 0
        max_len = 0
        for c in s:
            if c == '0':
                if ones > 0:
                    max_len = max(max_len, min(zeros, ones) << 1)
                    ones = 0
                    zeros = 1
                else:
                    zeros += 1
            else:
                if zeros > 0:
                    ones += 1
                else:
                    ones = 0

        return max(max_len, min(zeros, ones) << 1)


print(Solution().find_the_longest_balanced_substring('01000111'))
