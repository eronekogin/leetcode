"""
https://leetcode.com/problems/rle-iterator/
"""


class RLEIterator:

    def __init__(self, encoding: list[int]):
        stack = []
        for i in range(len(encoding) - 1, -1, -2):
            stack.append([encoding[i - 1], encoding[i]])  # [frequency, char]

        self.stack = stack

    def next(self, n: int) -> int:
        remain = n
        while self.stack and remain > self.stack[-1][0]:
            remain -= self.stack.pop()[0]

        if self.stack:
            self.stack[-1][0] -= remain
            return self.stack[-1][-1]

        return -1  # no next char.
