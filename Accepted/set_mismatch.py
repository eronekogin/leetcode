"""
https://leetcode.com/problems/set-mismatch/
"""


from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup, missing = None, None
        for num in nums:
            t = abs(num) - 1
            if nums[t] < 0:
                dup = t + 1
            else:
                nums[t] *= -1

        for i, num in enumerate(nums):
            if num > 0:
                missing = i + 1
                break

        return [dup, missing]

    def findErrorNums2(self, nums: List[int]) -> List[int]:
        s, n = sum(set(nums)), len(nums)
        return [sum(nums) - s, (((1 + n) * n) >> 1) - s]


print(Solution().findErrorNums([8, 7, 3, 5, 3, 6, 1, 4]))
