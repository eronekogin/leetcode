"""
https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/description/
"""


class Solution:
    """
    Solution
    """

    def max_score_indices(self, nums: list[int]) -> list[int]:
        """
        max_score_indices
        """
        zeros, ones = 0, nums.count(1)
        max_score = -1
        candidates: list[int] = []
        n = len(nums)
        for i in range(0, n):
            curr_score = zeros + ones
            if curr_score > max_score:
                candidates = [i]
                max_score = curr_score
            elif curr_score == max_score:
                candidates.append(i)

            zeros += nums[i] == 0
            ones -= nums[i] == 1

        # Handle last index.
        if zeros + ones > max_score:
            return [n]
        elif zeros + ones == max_score:
            return candidates + [n]
        else:
            return candidates
