"""
https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/
"""


from random import choice
from collections import defaultdict


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []  # The list to store all the numbers.
        self.idxs = defaultdict(set)  # val: set of indexes.

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection
        did not already contain the specified element.
        """
        self.idxs[val].add(len(self.nums))
        self.nums.append(val)
        return len(self.idxs[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection.
        Returns true if the collection contained the specified element.
        """
        if not self.idxs[val]:
            return False

        replaceIdx = self.idxs[val].pop()
        replaceVal = self.nums[-1]
        self.nums[replaceIdx] = replaceVal
        self.idxs[replaceVal].add(replaceIdx)
        self.idxs[replaceVal].discard(len(self.nums) - 1)
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return choice(self.nums)


r = RandomizedCollection()
r.insert(1)
r.insert(1)
r.insert(2)
r.getRandom()
r.remove(1)
r.getRandom()
