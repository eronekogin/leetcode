"""
https://leetcode.com/problems/circular-array-loop/
"""


from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        if not nums:
            return False

        n = len(nums)
        if n < 2:
            return False

        def move(src: int) -> int:
            return (src + nums[src]) % n

        # Take each number as the start of the cycle.
        for i in range(n):
            if nums[i]:  # Index i has not been visited yet.
                slow = i
                fast = move(slow)
                while nums[slow] * nums[fast] > 0 and\
                        nums[slow] * nums[move(fast)] > 0:
                    if slow == fast:
                        if slow == move(slow):
                            break  # Skip one element loop.

                        return True  # Found a cycle.

                    slow = move(slow)
                    fast = move(move(fast))

                # When coming here, no loop has been detected by the path
                # started from i, so mark all the elements on that path to 0
                # to indicate no loop.
                slow, sign = i, nums[i]
                while sign * nums[slow] > 0:
                    nums[slow], slow = 0, move(slow)

        return False  # Not any cycle found in nums.
