"""
https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/
"""


from collections import Counter


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        """
        1. If after flipping, some rows become all zeros while some rows become
            all ones, the zero rows should be the same before flipping while
            the one rows should be the totally opposite to the zero rows before
            flipping.
        2. Then the problem becomes to count the row which has the most number
            of same + opposite rows to itself.
        """
        patterns = Counter()
        for row in matrix:
            # c ^ row[0] means:
            # 1. if row[0] is zero, do not flip the remaining
            #   numbers in the current row.
            # 2. if row[0] is one, flip the current row to see if it is the
            #   same as some row occurred before.
            pattern = [c ^ row[0] for c in row]
            patterns[tuple(pattern)] += 1

        return max(patterns.values())
