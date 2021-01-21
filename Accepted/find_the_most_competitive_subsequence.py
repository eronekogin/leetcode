"""
https://leetcode.com/problems/find-the-most-competitive-subsequence/
"""


from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        N = len(nums) - 1
        if N + 1 == k:
            return nums

        stack = []
        for i, num in enumerate(nums):
            while stack and num < stack[-1] and len(stack) + N - i >= k:
                # When we still have enough numbers to be pushed into the
                # stack.
                stack.pop()

            if len(stack) < k:  # Add a new number to the rslt.
                stack.append(num)

        return stack


print(Solution().mostCompetitive([2, 4, 3, 3, 5, 4, 9, 6], 4))
