"""
https://leetcode.com/problems/min-stack/
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x: int) -> None:
        if self.min is None or x <= self.min:
            self.stack.append(self.min)
            self.min = x

        self.stack.append(x)

    def pop(self) -> None:
        if self.min == self.stack.pop():
            self.min = self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min


ms = MinStack()
ms.push(-2)
ms.push(0)
ms.push(-3)
print(ms.getMin())
ms.pop()
ms.top()
print(ms.getMin())
