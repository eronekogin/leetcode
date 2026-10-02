"""
https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/description/
"""


class Solution:
    """
    Solution
    """

    def number_of_substrings(self, s: str) -> int:
        """
        number of substrings
        """
        n = len(s)
        prev_zero_indexes = [-1] * (n + 1)
        for i in range(n):
            if i == 0 or s[i - 1] == '0':
                prev_zero_indexes[i + 1] = i
            else:
                prev_zero_indexes[i + 1] = prev_zero_indexes[i]

        rslt = 0

        for end in range(1, n + 1):
            c0 = 1 if s[end - 1] == '0' else 0

            start = end
            while start > 0 and c0 * c0 <= n:
                c1 = end - prev_zero_indexes[start] - c0

                if c0 * c0 <= c1:
                    rslt += min(
                        start - prev_zero_indexes[start],
                        c1 - c0 * c0 + 1
                    )

                start = prev_zero_indexes[start]
                c0 += 1

        return rslt
