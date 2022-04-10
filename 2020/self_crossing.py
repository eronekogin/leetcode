"""
https://leetcode.com/problems/self-crossing/
"""


from typing import List


class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        """
        Two cases:

                    b                              b
            +----------------+             +----------------+
            |                |             |                |
            |                |             |                | a
          c |                |           c |                |
            |                | a           |                |    f
            +----------->    |             |                | <----+
                    d        |             |                |      | e
                             |             |                       |
                                           +-----------------------+
                                                   d
        """
        b = c = d = e = 0
        for a in x:
            if d >= b > 0 and (a >= c or a >= c - e >= 0 and f >= d - b):
                return True

            b, c, d, e, f = a, b, c, d, e  # Check for the next line.

        return False
