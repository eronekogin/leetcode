"""
https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special/description/
"""


from math import ceil


class Solution:
    """
    Solution
    """

    def non_special_count(self, l: int, r: int) -> int:
        """
        non special count
        """
        # Create sieve to get prime p and a special number
        # is p * p since it only has 1, p as its two proper
        # divisors without itself.
        sr = int(r ** 0.5) + 1
        sieve = [1] * sr
        sieve[0] = sieve[1] = 0
        for i in range(2, sr):
            if sieve[i]:
                for j in range(i * i, sr, i):
                    sieve[j] = 0

        specials = sum(sieve[ceil(l ** 0.5): sr])

        return r - l + 1 - specials


print(Solution().non_special_count(5, 7))
