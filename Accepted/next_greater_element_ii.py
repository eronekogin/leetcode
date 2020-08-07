"""
https://leetcode.com/problems/next-greater-element-ii/
"""


from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        Brutal force, simply scan the whole list for each list item.
        """
        n = len(nums)
        rslt = [-1] * n
        for i, num in enumerate(nums):
            j = i + 1
            while j < n and nums[j] <= num:
                j += 1

            if j < n:
                rslt[i] = nums[j]
            else:
                j = j - n
                while j < i and nums[j] <= num:
                    j += 1

                if j < i:
                    rslt[i] = nums[j]

        return rslt

    def nextGreaterElements2(self, nums: List[int]) -> List[int]:
        """
        Scan the circular list from right to left and use a stack to store
        the latest next greater element.
        """
        n = len(nums)
        rslt, stack = [-1] * n, []
        for i in range((n << 1) - 1, -1, -1):
            actualIdx = i % n
            while stack and nums[stack[-1]] <= nums[actualIdx]:
                stack.pop()

            if stack:
                rslt[actualIdx] = nums[stack[-1]]

            stack.append(actualIdx)

        return rslt
