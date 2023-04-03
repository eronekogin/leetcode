"""
https://leetcode.com/problems/maximum-score-of-a-good-subarray/
"""


class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        maxScore = minNum = nums[k]
        l = r = k
        n = len(nums)
        while l > 0 or r < n - 1:
            left = nums[l - 1] if l > 0 else 0
            right = nums[r + 1] if r < n - 1 else 0

            if left < right:
                r += 1
            else:
                l -= 1

            minNum = min(minNum, nums[l], nums[r])
            maxScore = max(maxScore, minNum * (r - l + 1))

        return maxScore
