"""
https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/description/
"""


class Solution:
    """
    Solution
    """

    def find_score(self, nums: list[int]) -> int:
        """
        find score
        """
        n = len(nums)
        score = 0
        i = 0

        while i < n:
            start = i
            while i + 1 < n and nums[i + 1] < nums[i]:
                i += 1

            end = i
            while end >= start:
                score += nums[end]
                end -= 2  # Skip its left neighbour.

            i += 2  # Skip its right neigbour.

        return score


print(Solution().find_score(
    [10, 44, 10, 8, 48, 30, 17, 38, 41, 27, 16, 33, 45, 45, 34, 30, 22, 3, 42, 42]))
