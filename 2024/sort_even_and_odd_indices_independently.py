"""
https://leetcode.com/problems/sort-even-and-odd-indices-independently/description/
"""


class Solution:
    """
    Solution
    """

    def sort_even_odd(self, nums: list[int]) -> list[int]:
        """
        sort_even_odd
        """
        odds = [x for i, x in enumerate(nums) if i & 1]
        evens = [x for i, x in enumerate(nums) if i & 1 == 0]
        odds.sort(reverse=True)
        evens.sort()

        rslt: list[int] = [0] * len(nums)
        j1 = j2 = 0
        for i in range(len(nums)):
            if i & 1:
                rslt[i] = odds[j1]
                j1 += 1
            else:
                rslt[i] = evens[j2]
                j2 += 1

        return rslt
