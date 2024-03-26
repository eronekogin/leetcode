"""
https://leetcode.com/problems/replace-non-coprime-numbers-in-array/description/
"""


from math import gcd


class Solution:
    """
    Solution
    """

    def replace_non_coprimes(self, nums: list[int]) -> list[int]:
        """
        replace non co primes
        """
        rslt: list[int] = []
        for x in nums:
            curr_lcm = x
            while True:
                g = gcd(rslt[-1] if rslt else 1, curr_lcm)
                if g == 1:  # Co prime
                    break

                curr_lcm *= rslt.pop() // g

            rslt.append(curr_lcm)

        return rslt


print(Solution().replace_non_coprimes(
    [287, 41, 49, 287, 899, 23, 23, 20677, 5, 825]
))
