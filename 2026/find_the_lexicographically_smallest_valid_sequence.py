"""
https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/description/
"""


class Solution:
    """
    Solution
    """

    def valid_sequence(self, word1: str, word2: str) -> list[int]:
        """
        valid sequence
        """
        n, m = len(word1), len(word2)
        last = [-1] * m
        i2 = m - 1

        for i1 in range(n - 1, -1, -1):
            if i2 >= 0 and word1[i1] == word2[i2]:
                last[i2] = i1
                i2 -= 1

        i2 = 0
        skip_times = 0
        rslt: list[int] = []

        for i1, c in enumerate(word1):
            if i2 == m:
                break

            if (
                c == word2[i2] or
                skip_times == 0 and
                (i2 == m - 1 or i1 < last[i2 + 1])
            ):
                skip_times += c != word2[i2]
                rslt.append(i1)
                i2 += 1

        if i2 == m:
            return rslt

        return []


print(Solution().valid_sequence("cdbbcdddddbdddbcdbdbbbccbbc", "dbc"))
