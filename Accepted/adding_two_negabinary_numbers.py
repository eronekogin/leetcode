"""
https://leetcode.com/problems/adding-two-negabinary-numbers/
"""


class Solution:
    def addNegabinary(self, arr1: list[int], arr2: list[int]) -> list[int]:
        rslt = []
        carry = 0
        while arr1 or arr2 or carry:
            carry += (arr1 or [0]).pop() + (arr2 or [0]).pop()
            rslt.append(carry & 1)
            carry = -(carry >> 1)

        while len(rslt) > 1 and rslt[-1] == 0:  # Remove leading zeros.
            rslt.pop()

        return rslt[::-1]
