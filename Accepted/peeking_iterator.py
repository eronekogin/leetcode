"""
https://leetcode.com/problems/peeking-iterator/
"""


from typing import List


class Iterator:
    def __init__(self, nums: List[int]):
        self.nums = nums[::-1]

    def hasNext(self) -> bool:
        return len(self.nums) > 0

    def next(self) -> int:
        return self.nums.pop()


class PeekingIterator:
    """
    Store the next value outside the iterator. When next is called return the 
    stored value and populate with next value from iterator.
    """

    def __init__(self, iterator: Iterator):
        self.iter = iterator
        self.curr = self.iter.next() if self.iter.hasNext() else None

    def peek(self) -> int:
        return self.curr

    def next(self) -> int:
        rslt = self.curr
        self.curr = self.iter.next() if self.iter.hasNext() else None
        return rslt

    def hasNext(self) -> bool:
        return self.curr is not None


i = PeekingIterator(Iterator([1, 2, 3]))
print(i.next())
print(i.peek())
print(i.next())
print(i.next())
print(i.hasNext())
