"""
https://leetcode.com/problems/plus-one/
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)):
            newVal = digits[~i] + carry
            carry = newVal // 10
            digits[~i] = newVal % 10
            if not carry:
                break

        if carry:
            return [1] + digits

        return digits


digits = [1, 2, 3]
print(Solution().plusOne(digits))
