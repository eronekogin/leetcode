"""
https://leetcode.com/problems/reach-end-of-array-with-max-score/description/
"""


class Solution:
    """
    Solution
    """
    def find_maximum_score(self, nums: list[int]) -> int:
        """
        find maximum score
        """
        start = end = 0
        score = 0

        for end, x in enumerate(nums):
            if x <= nums[start]:
                continue

            score += nums[start] * (end - start)
            start = end

        return score + nums[start] * (end - start)


print(Solution().find_maximum_score([1,3,1,5]))
