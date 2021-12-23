"""
https://leetcode.com/problems/fizz-buzz-multithreaded/
"""


from threading import Semaphore


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.done = False
        self.fSem = Semaphore(0)
        self.bSem = Semaphore(0)
        self.fbSem = Semaphore(0)
        self.nSem = Semaphore(1)

    def fizz(self, printFizz) -> None:
        while True:
            self.fSem.acquire()
            if self.done:
                break

            printFizz()
            self.nSem.release()

    def buzz(self, printBuzz) -> None:
        while True:
            self.bSem.acquire()
            if self.done:
                break

            printBuzz()
            self.nSem.release()

    def fizzbuzz(self, printFizzBuzz) -> None:
        while True:
            self.fbSem.acquire()
            if self.done:
                break

            printFizzBuzz()
            self.nSem.release()

    def number(self, printNumber) -> None:
        # loop on numbers.
        for i in range(1, self.n + 1):
            self.nSem.acquire()
            if i % 15 == 0:
                self.fbSem.release()
            elif i % 3 == 0:
                self.fSem.release()
            elif i % 5 == 0:
                self.bSem.release()
            else:
                printNumber(i)
                self.nSem.release()

        # When loop ends.
        # Needed so the remaining logic only executes once.
        self.nSem.acquire()

        # Set the flag to done.
        self.done = True

        # Then let the remaining threads exit.
        self.fSem.release()
        self.bSem.release()
        self.fbSem.release()
