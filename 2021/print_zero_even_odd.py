"""
https://leetcode.com/problems/print-zero-even-odd/
"""


from threading import Barrier, Lock


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.barriers = [Barrier(2), Barrier(2)]
        self.cnt = 0
        self.zeroLock = Lock()

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n):
            self.zeroLock.acquire()
            printNumber(0)
            self.cnt += 1
            self.barriers[self.cnt & 1].wait()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n >> 1):
            self.barriers[0].wait()
            printNumber(self.cnt)
            self.zeroLock.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range((self.n + 1) >> 1):
            self.barriers[1].wait()
            printNumber(self.cnt)
            self.zeroLock.release()
