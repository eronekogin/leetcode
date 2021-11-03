"""
https://leetcode.com/problems/print-foobar-alternately/
"""


from threading import Barrier


class FooBar:
    def __init__(self, n):
        self.n = n
        self.barrier = Barrier(2)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.barrier.wait()  # foo
            printFoo()
            self.barrier.wait()  # bar

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.barrier.wait()  # foo
            self.barrier.wait()  # bar
            printBar()
