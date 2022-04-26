"""
https://leetcode.com/problems/design-a-stack-with-increment-operation/
"""


class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) == self.maxSize:
            return

        self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1

        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        if k >= len(self.stack):
            self.stack = [x + val for x in self.stack]
        else:
            for i in range(k):
                self.stack[i] += val
