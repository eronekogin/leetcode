"""
https://leetcode.com/problems/array-nesting/
"""


from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = set()
        maxLen = 0
        for num in nums:
            if num not in visited:
                # Calculate the length of the new set.
                start = num
                end = nums[num]
                setLen = 1
                visited.add(num)
                while end != start:
                    visited.add(end)
                    setLen += 1
                    end = nums[end]

                maxLen = max(maxLen, setLen)

        return maxLen
