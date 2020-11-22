"""
https://leetcode.com/problems/numbers-at-most-n-given-digit-set/
"""


from typing import List


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        maxLen, options = len(s), len(digits)

        # All the numbers with less length than s satisfy the condition. For
        # those numbers, each position could pick all the choices from digits.
        rslt = sum(options ** i for i in range(1, maxLen))

        # Now consider the numbers with the same length as s.
        for i, c in enumerate(s):
            # For all the numbers with the ith digit less than s[i], the
            # remaining positions could take any option.
            rslt += sum(option < c for option in digits) * (
                options ** (maxLen - i - 1))

            if c not in digits:  # Cannot write any new number with length as s.
                return rslt

            # When coming here, the current digit in s is in digits, so we
            # continue to check the next digit in s to determine the choices.

        # When coming here, all the digits in s are in digits, this adds 1
        # choice to the final result.
        return rslt + 1
