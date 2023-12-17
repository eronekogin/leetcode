"""
https://leetcode.com/problems/range-frequency-queries/
"""


from collections import defaultdict
from bisect import bisect_right


class RangeFreqQuery:
    """
    RangeFreqQuery
    """

    def __init__(self, arr: list[int]):
        cnt: defaultdict[int, list] = defaultdict(list)
        for i, x in enumerate(arr):
            cnt[x].append(i)

        self.cnt = cnt

    def query(self, left: int, right: int, value: int) -> int:
        """
        query
        """
        i = bisect_right(self.cnt[value], left - 1)
        j = bisect_right(self.cnt[value], right)
        return j - i
