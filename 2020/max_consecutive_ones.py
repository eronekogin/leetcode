"""
https://leetcode.com/problems/max-consecutive-ones/
"""


from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currOnes = maxOnes = 0
        for num in nums:
            if num:
                currOnes += 1
            else:
                maxOnes = max(maxOnes, currOnes)
                currOnes = 0

        return max(maxOnes, currOnes)


print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
