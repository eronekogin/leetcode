"""
https://leetcode.com/problems/insert-delete-getrandom-o1/
"""


from random import choice


class RandomizedSet:
    """
    Presumption: All the provided numbers are unique.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []  # A list to hold all the current numbers.
        self.idxes = {}  # number: index

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set.
        Returns true if the set did not already contain the specified element.
        """
        if val in self.idxes:
            return False

        self.nums.append(val)
        self.idxes[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set.
        Returns true if the set contained the specified element.
        """
        if val not in self.idxes:
            return False

        replaceIdx = self.idxes[val]
        replaceVal = self.nums[-1]
        self.idxes[replaceVal] = replaceIdx
        self.nums[replaceIdx] = replaceVal
        self.idxes.pop(val)
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.nums)
