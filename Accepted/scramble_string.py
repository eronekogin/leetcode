"""
https://leetcode.com/problems/scramble-string/
"""


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        def f(s1: str, s2: str) -> bool:
            rslt = False
            if (s1, s2) not in memo:
                if s1 == s2:
                    rslt = True
                elif len(s1) != len(s2) or set(s1) != set(s2):
                    pass
                else:
                    for i in range(1, len(s1)):
                        # x1 == y1 and x2 == y2.
                        # or x1 == y2 and x2 == y1.
                        if (f(s1[:i], s2[:i]) and f(s1[i:], s2[i:])) or (
                                f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i])):
                            rslt = True
                            break

                memo[(s1, s2)] = rslt

            return memo[(s1, s2)]

        memo = {}
        return f(s1, s2)
