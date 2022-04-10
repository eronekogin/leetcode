"""
https://leetcode.com/problems/online-majority-element-in-subarray/
"""


from collections import defaultdict
from bisect import bisect_left, bisect_right
from random import randint


class MajorityChecker:
    """
    1. Save all index of occurrence x in the input list into x2i[x], so that
        when we need to find how many x between a range [left, right], we could
        binary search the index array to get the left boundary l and right
        boundary r, the total number of occurrences of x = r - l
    2. Since threshold must be greater than the half of the length of
        the range, we have 50% to find a majority element when we randomly
        pick a number from the target range. We try to guess 20 times at most
        to pick up a random number from the range and each time we have
        1/2^20 chance to miss it. Since the query is only called 10000 times,
        the match rate is quite acceptable.
    """

    def __init__(self, arr: list[int]):
        x2i = defaultdict(list)
        for i, x in enumerate(arr):
            x2i[x].append(i)

        self.A = arr
        self.x2i = x2i

    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(20):
            x = self.A[randint(left, right)]
            l = bisect_left(self.x2i[x], left)
            r = bisect_right(self.x2i[x], right)
            if r - l >= threshold:
                return x

        return -1  # Not found.
