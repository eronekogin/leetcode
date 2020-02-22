"""
https://leetcode.com/problems/find-the-duplicate-number/
"""


from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Use slow and fast pointers to detect a cycle in the input array and
        the entry of the cycle will be the duplicate number.

        For more details, look at linked_list_cycle_ii.py
        """
        slow, fast = nums[0], nums[nums[0]]

        # Find the intersection point of the two runners.
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # Find the entrance point to the cycle.
        slow, fast = nums[0], nums[fast]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


print(Solution().findDuplicate([1, 3, 4, 2, 2]))
