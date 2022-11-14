"""
https://leetcode.com/problems/design-an-ordered-stream/
"""


class OrderedStream:

    def __init__(self, n: int):
        self.maxSize = n
        self.items: list[str] = ['' for _ in range(n)]
        self.currIndex = 0

    def insert(self, idKey: int, value: str) -> list[str]:
        self.items[idKey - 1] = value
        rslt: list[str] = []
        start = self.currIndex
        while start < self.maxSize and self.items[start] != '':
            rslt.append(self.items[start])
            start += 1

        self.currIndex = start
        return rslt
