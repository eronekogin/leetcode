"""
https://leetcode.com/problems/the-dining-philosophers/
"""


from threading import Semaphore


class DiningPhilosophers:
    """
    Simple solution, make sure only 4 forks could be picked up at most, in
    order to prevent the deadlock case when 5 forks are picked up by each
    philosopher and no one is able to eat.
    """

    def __init__(self) -> None:
        self.sizeLock = Semaphore(4)
        self.locks = [Semaphore(1) for _ in range(5)]

    def wantsToEat(
        self,
        philosopher: int,
        pickLeftFork,
        pickRightFork,
        eat,
        putLeftFork,
        putRightFork,
    ) -> None:
        left, right = philosopher, (philosopher - 1) % 5
        with self.sizeLock:
            with self.locks[left], self.locks[right]:
                pickLeftFork()
                pickRightFork()
                eat()
                putLeftFork()
                putRightFork()
