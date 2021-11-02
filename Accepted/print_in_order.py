"""
https://leetcode.com/problems/print-in-order/
"""

from threading import Barrier


class Foo:
    def __init__(self):
        self.first_barrier = Barrier(2)
        self.second_barrier = Barrier(2)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.first_barrier.wait()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.first_barrier.wait()
        printSecond()
        self.second_barrier.wait()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.second_barrier.wait()
        printThird()
