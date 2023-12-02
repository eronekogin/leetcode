"""
https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/
"""


from functools import cache


class Solution:
    """
    Solution
    """

    def possibly_equals(self, s1: str, s2: str) -> bool:
        """
        possibly_equals
        """
        def get_lengths(s: str):
            """
            Input string stands for the compressed length of some sub strings from the
            original string, for example, if s == '123', it could have the following
            combinations:
                1 + 23: 1 char + 23 chars
                12 + 3: 12 chars + 3 chars

            So this function generates all possible lengths of this compressed strings.
            """
            rslt = {int(s)}
            for i in range(1, len(s)):
                rslt |= {
                    x + y
                    for x in get_lengths(s[:i])
                    for y in get_lengths(s[i:])
                }

            return rslt

        @cache
        def dfs(i: int, j: int, diff: int):
            """
            diff stands for the difference found from s1 and s2:
                diff > 0: s1 has more difference than s2
                diff < 0: s2 has more difference than s1
            """
            if i == len(s1) and j == len(s2):
                return diff == 0

            if i < len(s1) and s1[i].isdigit():
                digit_end = i
                while digit_end < len(s1) and s1[digit_end].isdigit():
                    digit_end += 1

                for x in get_lengths(s1[i: digit_end]):
                    if dfs(digit_end, j, diff - x):
                        return True
            elif j < len(s2) and s2[j].isdigit():
                digit_end = j
                while digit_end < len(s2) and s2[digit_end].isdigit():
                    digit_end += 1

                for x in get_lengths(s2[j: digit_end]):
                    if dfs(i, digit_end, diff + x):
                        return True
            elif diff == 0:
                if i < len(s1) and j < len(s2) and s1[i] == s2[j]:
                    return dfs(i + 1, j + 1, diff)
            elif diff > 0:
                if i < len(s1):
                    return dfs(i + 1, j, diff - 1)
            else:
                if j < len(s2):
                    return dfs(i, j + 1, diff + 1)

            return False

        return dfs(0, 0, 0)
