"""
https://leetcode.com/problems/number-of-different-subsequences-gcds/
"""


from math import gcd


class Solution:
    def countDifferentSubsequenceGCDs(self, nums: list[int]) -> int:
        """
        It just needs to find the unique gcd from any non-empty subsequence,
        which means each subsequence at least should contain 1 number. And
        for possible divisors in nums, the range could be from 1 to the
        maximum number in nums. So we can scan this range and check if any
        number between the above range can be a gcd of some numbers in nums.
        """
        maxLimit = max(nums) + 1
        divisors = set(nums)
        rslt = 0

        for x in range(1, maxLimit):
            g = 0
            for y in range(x, maxLimit, x):
                if y in divisors:
                    g = gcd(g, y)

                if g == x:
                    break

            if g == x:
                rslt += 1

        return rslt
