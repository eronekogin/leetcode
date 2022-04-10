"""
https://leetcode.com/problems/building-h2o/
"""


from threading import Semaphore, Barrier


class H2O:
    def __init__(self):
        self.semH = Semaphore(2)
        self.semO = Semaphore(1)
        self.barrier = Barrier(3)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.semH:
            self.barrier.wait()
            releaseHydrogen()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.semO:
            self.barrier.wait()
            releaseOxygen()
