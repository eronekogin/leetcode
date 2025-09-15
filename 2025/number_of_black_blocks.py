"""
https://leetcode.com/problems/number-of-black-blocks/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def count_black_blocks(self, m: int, n: int, coordinates: list[list[int]]) -> list[int]:
        """
        count black blocks
        """
        cnt = Counter()
        rslt = [(m - 1) * (n - 1), 0, 0, 0, 0]
        for r, c in coordinates:
            for nr, nc in [(r, c), (r + 1, c), (r, c + 1), (r + 1, c + 1)]:
                if 0 < nr < m and 0 < nc < n:
                    rslt[cnt[(nr, nc)]] -= 1
                    cnt[(nr, nc)] += 1
                    rslt[cnt[(nr, nc)]] += 1

        return rslt
