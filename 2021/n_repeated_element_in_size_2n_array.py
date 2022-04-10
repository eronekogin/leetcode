"""
https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
"""


class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        visited = set()
        for num in nums:
            if num in visited:
                return num

            visited.add(num)
