"""
https://leetcode.com/problems/backspace-string-compare/
"""


from itertools import zip_longest


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def gen(s: str) -> str:
            """
            Start to check from the end of the input string s,
            so that we could make sure the non-# char will stay
            in the final reduced result. Then if we come across
            a #, we skip the next char if any.
            """
            back = 0
            for c in reversed(s):
                if c == '#':
                    back += 1
                elif back:
                    back -= 1
                else:
                    yield c

        return all([cs == ct for cs, ct in zip_longest(gen(S), gen(T))])
