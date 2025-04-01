"""
https://leetcode.com/problems/subsequence-with-the-minimum-score/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_score(self, s: str, t: str) -> int:
        """
        minimum score
        """
        # Check if t is already a subsequence of s.
        j = 0
        nt = len(t)
        ns = len(s)
        for c in s:
            if c == t[j]:
                j += 1

            if j == nt:
                return 0

        # Index of the first char to be removed from t when
        # s ends at index i.
        first_removed_from_left = [0] * ns
        j = 0
        for i, c in enumerate(s):
            if c == t[j]:
                j += 1

            first_removed_from_left[i] = j

        min_score = nt  # Worst case is to remove all chars from t.
        j = nt - 1

        # Check from rigth to left
        for i in range(ns - 1, -1, -1):
            if j >= first_removed_from_left[i]:
                min_score = min(
                    min_score,
                    j - first_removed_from_left[i] + 1
                )

            if s[i] == t[j]:
                j -= 1

            # Also check the score to remove all chars from index 0 to j.
            min_score = min(
                min_score,
                j + 1
            )

        return min_score
