"""
https://leetcode.com/problems/design-front-middle-back-queue/
"""

from collections import deque


class FrontMiddleBackQueue:

    def __init__(self):
        self.leftPart: deque[int] = deque()
        self.rightPart: deque[int] = deque()

    def _balance(self):
        # Always keeps left part greater than right part in order to
        # return/insert the required middle value.
        if len(self.leftPart) > len(self.rightPart) + 1:
            self.rightPart.appendleft(self.leftPart.pop())

        if len(self.leftPart) < len(self.rightPart):
            self.leftPart.append(self.rightPart.popleft())

    def pushFront(self, val: int):
        self.leftPart.appendleft(val)
        self._balance()

    def pushMiddle(self, val: int):
        if len(self.leftPart) > len(self.rightPart):
            self.rightPart.appendleft(self.leftPart.pop())

        self.leftPart.append(val)

    def pushBack(self, val: int):
        self.rightPart.append(val)
        self._balance()

    def popFront(self):
        if not self.leftPart:
            return -1

        rslt = self.leftPart.popleft()
        self._balance()
        return rslt

    def popMiddle(self):
        rslt = (self.leftPart or [-1]).pop()
        self._balance()
        return rslt

    def popBack(self):
        rslt = (self.rightPart or self.leftPart or [-1]).pop()
        self._balance()
        return rslt
