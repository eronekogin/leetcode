"""
https://leetcode.com/problems/design-bitset/description/
"""


class Bitset:

    def __init__(self, size: int):
        self.bits: list[int] = [0] * size
        self.is_flipped = False
        self.ones = 0

    def fix(self, idx: int) -> None:
        if self.is_flipped:
            if self.bits[idx] == 1:
                self.ones += 1

            self.bits[idx] = 0
        else:
            if self.bits[idx] == 0:
                self.ones += 1

            self.bits[idx] = 1

    def unfix(self, idx: int) -> None:
        if self.is_flipped:
            if self.bits[idx] == 0:
                self.ones -= 1

            self.bits[idx] = 1
        else:
            if self.bits[idx] == 1:
                self.ones -= 1

            self.bits[idx] = 0

    def flip(self) -> None:
        self.is_flipped = not self.is_flipped
        self.ones = len(self.bits) - self.ones

    def all(self) -> bool:
        return self.ones == len(self.bits)

    def one(self) -> bool:
        return self.ones > 0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        return ''.join(
            str(1 - i) if self.is_flipped else str(i)
            for i in self.bits
        )
