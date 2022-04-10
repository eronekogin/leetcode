"""
https://leetcode.com/problems/single-number-ii/
"""


from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        For any number x in nums:
        x1 x2
        -- --
        x  0
        0  x
        0  0

        So if x only occurs once, it must be stored in x1 in the end.

        Check https://leetcode.com/problems/single-number-ii/discuss/43295/Detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers
        for a general solution.
        """
        x1 = x2 = 0
        for num in nums:
            x1 = (x1 ^ num) & ~x2
            x2 = (x2 ^ num) & ~x1

        return x1
