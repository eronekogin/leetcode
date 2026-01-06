"""
https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def get_words_in_longest_subsequence(self, words: list[str], groups: list[int]) -> list[str]:
        """
        Docstring for get_words_in_longest_subsequence

        :param self: Description
        :param words: Description
        :type words: list[str]
        :param groups: Description
        :type groups: list[int]
        :return: Description
        :rtype: list[str]
        """
        def is_candidate(w1: str, w2: str) -> bool:
            return len(w1) == len(w2) and sum(x != y for x, y in zip(w1, w2)) == 1

        n = len(words)
        dp = [1] * n
        prev = [-1] * n
        max_index = 0

        for end in range(1, n):
            for start in range(end):
                if (
                    is_candidate(words[start], words[end]) and
                    dp[start] + 1 > dp[end] and
                    groups[start] != groups[end]
                ):
                    dp[end] = dp[start] + 1
                    prev[end] = start

            if dp[end] > dp[max_index]:
                max_index = end

        rslt: list[str] = []
        i = max_index
        while i >= 0:
            rslt.append(words[i])
            i = prev[i]

        rslt.reverse()
        return rslt
