"""
https://leetcode.com/problems/finding-3-digit-even-numbers/
"""


from itertools import permutations


class Solution:
    """
    Solution
    """

    def find_even_numbers(self, digits: list[int]) -> list[int]:
        """
        find_even_numbers
        """
        rslt = set()
        for x, y, z in permutations(digits, 3):
            if x != 0 and z & 1 == 0:
                rslt.add(x * 100 + y * 10 + z)

        return sorted(rslt)
