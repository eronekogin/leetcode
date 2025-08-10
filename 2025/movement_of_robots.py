"""
https://leetcode.com/problems/movement-of-robots/description/
"""


class Solution:
    """
    Solution
    """

    def sum_distance(self, nums: list[int], s: str, d: int) -> int:
        """
        Key point is that two robots collide does not impact their
        walking distance, if a robot turn its direction, it can be
        taken as the other robot who collided with him walk toward
        its original direction.
        """
        for i, x in enumerate(nums):
            if s[i] == 'R':
                nums[i] = x + d
            else:
                nums[i] = x - d

        nums.sort()
        rslt = 0
        mod = 10 ** 9 + 7
        curr_sum = 0
        for i, x in enumerate(nums):
            rslt += x * i - curr_sum
            curr_sum += x
            rslt %= mod
            curr_sum %= mod

        return rslt % mod
