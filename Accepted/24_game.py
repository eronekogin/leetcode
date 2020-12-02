"""
https://leetcode.com/problems/24-game/
"""


from typing import List


from itertools import permutations
from math import isclose


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        """
        1. Simply enumearte on all the combination of nums.
        2. If only 1 item left in nums, check if it is 24.
        3. When b is zero, b and a / b will simply return 0. So we could
            avoid the zero-divide issue.
        """
        if len(nums) == 1:
            return isclose(nums[0], 24)

        return any(
            self.judgePoint24([x] + remain)
            for a, b, *remain in permutations(nums)
            for x in {a + b, a - b, a * b, b and a / b})
