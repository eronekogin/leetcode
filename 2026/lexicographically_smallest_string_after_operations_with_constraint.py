"""
https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/description/
"""


class Solution:
    """
    Solution
    """

    def get_smallest_string(self, s: str, k: int) -> str:
        """
        get smallest string
        """
        rslt = list(s)
        offset = ord('a')
        remain = k

        for i, c in enumerate(rslt):
            if c == 'a':
                continue

            curr = ord(c)
            d = min(curr - offset, 26 - curr + offset)

            if d <= remain:
                rslt[i] = 'a'
                remain -= d
            else:
                rslt[i] = chr(curr - remain)
                break

        return ''.join(rslt)


print(Solution().get_smallest_string("xaxcd", 4))
