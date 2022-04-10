"""
https://leetcode.com/problems/number-of-recent-calls/
"""


from collections import deque


class RecentCounter:

    def __init__(self):
        self._requests = deque()

    def ping(self, t: int) -> int:
        start = t - 3000
        self._requests.append(t)
        while self._requests[0] < start:
            self._requests.popleft()

        return len(self._requests)
