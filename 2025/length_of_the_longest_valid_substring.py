"""
https://leetcode.com/problems/length-of-the-longest-valid-substring/description/
"""


class Solution:
    """
    Solution
    """

    def longest_valid_substring(self, word: str, forbidden: list[str]) -> int:
        """
        longest valid substring
        """
        forbidden_set = set(forbidden)

        max_len = 0

        r = len(word) - 1
        for l in range(len(word) - 1, -1, -1):
            for m in range(l, min(l + 10, r + 1)):
                if word[l: m + 1] in forbidden_set:
                    r = m - 1
                    break

            max_len = max(max_len, r - l + 1)

        return max_len


print(Solution().longest_valid_substring(
    "bcbab", ["cba", "aaab", "bcbc", "caba"]))
