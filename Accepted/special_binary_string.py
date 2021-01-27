"""
https://leetcode.com/problems/special-binary-string/
"""


class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        """
        1. Take '1' as '(' and '0' as ')', then a special string could be taken
            as a valid parentheses.
        2. A valid parentheses has two forms:
            2.1 Not embedded: () -> 10
            2.2 Embedded: (()) -> 1100
        3. Then if we come across ()(()) -> 101100, the largest form could be
            110010, which is (())(). In other words, the string with more
            leading '1's should come first in the largest form.
        4. In case we have embedded in the middle, like ()(( ()(()) )), we
            could use dfs to reorder each sub-level first, then reorder the
            outter level.
        """
        def do(start: int, end: int) -> str:
            if start >= end:
                return ''

            rslt, cnt = [], 0
            s = start
            for e in range(start, end):
                if S[e] == '1':
                    cnt += 1
                else:
                    cnt -= 1

                if not cnt:  # Found a special string.
                    rslt.append('1' + do(s + 1, e) + '0')
                    s = e + 1

            return ''.join(reversed(sorted(rslt)))

        return do(0, len(S))
