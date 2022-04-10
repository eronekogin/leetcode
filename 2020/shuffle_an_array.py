"""
https://leetcode.com/problems/shuffle-an-array/
"""


from typing import List
from random import randrange


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.originalNums = [_ for _ in nums]
        self.maxLen = len(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.originalNums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.

        Use Knuth-Durstenfeld Shuffle algorithm since we already know
        the total length of the input list.
        """
        nums, maxLen = self.nums, self.maxLen
        for i in reversed(range(maxLen)):
            r = randrange(0, i + 1)
            nums[r], nums[i] = nums[i], nums[r]

        return nums


s = Solution([1, 2, 3])
print(s.shuffle())
