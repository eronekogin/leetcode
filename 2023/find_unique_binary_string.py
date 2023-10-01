"""
https://leetcode.com/problems/find-unique-binary-string/
"""


class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        """
        Since all numbers in nums are unique, we can create a binary string which has each of its bit differs from the
        corresponding bit in the corresponding number, so that this new number is different than any other number
        in the list at least on one bit.
        """
        return ''.join(['1' if num[i] == '0' else '0' for i, num in enumerate(nums)])


        