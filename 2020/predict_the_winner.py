"""
https://leetcode.com/problems/predict-the-winner/
"""


from typing import List


class Solution:
    def PredictTheWinner1(self, nums: List[int]) -> bool:
        """
        Simply choose the number one player by another, calculate the total
        number by adding the number p1 chooses and subtracting the number p2
        chooses and see if the total number >= 0 to determine if p1 could win.
        """
        memo = {}  # (start, end): max total number between [start, end].

        def pick(start: int, end: int) -> int:
            if start == end:  # Only one item left to pick.
                return nums[start]

            if (start, end) not in memo:
                a = nums[start] - pick(start + 1, end)
                b = nums[end] - pick(start, end - 1)
                memo[(start, end)] = max(a, b)

            return memo[(start, end)]

        return pick(0, len(nums) - 1) >= 0


print(Solution().PredictTheWinner([1, 5, 233, 7]))
