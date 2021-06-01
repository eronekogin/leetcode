"""
https://leetcode.com/problems/bitwise-ors-of-subarrays/
"""


class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        """
        Simply scan all the sub arrays in order to find the unique rslts.
        """
        rslt, curr = set(), set()
        for num in arr:
            curr = {num | j for j in curr} | {num}
            rslt |= curr

        return len(rslt)
