"""
https://leetcode.com/problems/numbers-with-repeated-digits/
"""


from math import perm


class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        """
        1. Transfer the problem to find the total number of positive integers
            that have non-repeating digits.
        2. Suppose n has k digits:
            2.1 Find all the candidate numbers having less than k digits, then
                for i in range(1, k), each i digits have 9 * perm(9, i - 1)
                permutations. This is because the first digit could not be 0
                as leading zero is illegal, but the remaining digits could
                have zero.
            2.2 Then consider the numbers that having exactly k digits,
                suppose n = 8756, then we should check:
                2.2.1 1xxx to 7xxx
                2.2.2 80xx to 86xx
                2.2.3 870x to 874x
                2.2.4 8750 to 8756
        """
        # Padding n to n + 1 so that when checking the numbers having exactly
        # k digits, we don't need to pad any longer because of the range
        # function in python.
        digits = [int(c) for c in str(n + 1)]
        K = len(digits)
        cnt = 0

        # Count the number of non-repeating positive integers that have
        # less digits than K.
        for i in range(1, K):
            cnt += 9 * perm(9, i - 1)

        # Now count the number of non-repeating positive integers that
        # have exactly K digits.
        seen = set()
        for i, currDigit in enumerate(digits):
            for digit in range(0 if i else 1, currDigit):
                # Should not dup with the previous digits.
                if digit not in seen:
                    cnt += perm(10 - i - 1, K - i - 1)

            # Skip processing as the number itself has dup digits now.
            if currDigit in seen:
                break

            seen.add(currDigit)

        return n - cnt
