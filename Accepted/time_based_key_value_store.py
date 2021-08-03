"""
https://leetcode.com/problems/time-based-key-value-store/
"""

from bisect import bisect_right
from collections import defaultdict


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = defaultdict(list)
        self.memo = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append(timestamp)
        self.memo[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        candidates = self.keys[key]
        if not candidates:  # Not found.
            return ''

        i = bisect_right(candidates, timestamp)
        if i == 0:  # No candidate having timestamp less than the target.
            return ''

        return self.memo[candidates[i - 1]]


t = TimeMap()
t.set('foo', 'bar', 1)
t.get('foo', 1)
