"""
https://leetcode.com/problems/fancy-sequence/
"""


class Fancy:
    """
    Since we only do add or multiply operations on an integer, the result can
    be as follows if our original integer is represented by ax + b:

        Add: ax + b + inc = ax + (b + inc)
        Mul: (ax + b) * m = (am)x + bm

    So for each new value, instead of storing its original value, we store x
    to our list. So if ax + b = v, then x = (v - b) / a.

    In this case, when the getIndex is called right after a new value is
    appened, we could still get the right value by applying the same equation
    ax + b.
    """

    def __init__(self):
        self.x: list[int] = []
        self.a = 1
        self.b = 0
        self.MOD = 10 ** 9 + 7

    def append(self, val: int) -> None:
        self.x.append((val - self.b) * pow(self.a, -1, self.MOD))

    def addAll(self, inc: int) -> None:
        self.b += inc

    def multAll(self, m: int) -> None:
        self.a = self.a * m % self.MOD
        self.b = self.b * m % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.x):
            return -1

        return (self.a * self.x[idx] + self.b) % self.MOD


f = Fancy()
f.append(2)
f.addAll(3)
f.append(7)
f.multAll(2)
f.getIndex(0)
f.addAll(3)
f.append(10)
f.multAll(2)
f.getIndex(0)
f.getIndex(1)
f.getIndex(2)
