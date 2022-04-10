"""
https://leetcode.com/problems/combination-sum-iv/
"""


from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # When the target is zero while all the numbers in nums are
        # positive, the only combination is that we don't select any number.
        memo = {0: 1}  # target: combinations.

        def get_combinations(t: int) -> int:
            if t in memo:
                return memo[t]

            combinations = 0
            for num in nums:
                if t >= num:
                    combinations += get_combinations(t - num)

            memo[t] = combinations
            return combinations

        return get_combinations(target)


print(Solution().combinationSum4([1, 2, 3], 4))
