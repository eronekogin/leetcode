"""
https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/
"""


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        """
        In order to make A and B sub sequences has the minimum
        max(depth(A), depth(B)), the goal is to make A and B as even as
        possible.
        """
        d1 = d2 = 0
        rslt = [0] * len(seq)
        for i, c in enumerate(seq):
            if c == '(':
                v = 1
            else:
                v = -1

            if (v > 0) == (d1 < d2):
                d1 += v
            else:
                d2 += v
                rslt[i] = 1

        return rslt
