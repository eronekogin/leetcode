"""
https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/description/
"""


class Solution:
    """
    Solution
    """

    def number_of_subarrays(self, nums: list[int]) -> int:
        """
        number of subarrays
        """
        stack: list[list[int]] = []
        pairs = 0

        for x in nums:
            while stack and stack[-1][0] < x:
                stack.pop()

            if not stack or stack[-1][0] > x:
                stack.append([x, 0])

            stack[-1][1] += 1

            # The current x can form a new subarray with any
            # pre-existing x
            pairs += stack[-1][1]

        return pairs
