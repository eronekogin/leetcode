"""
https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_numbers(self, num: int, k: int) -> int:
        """
        minimum numbers
        """
        if num == 0:
            return 0

        target = num % 10

        for i in range(1, 11):
            curr = i * k
            if curr > num:
                return -1

            if curr % 10 == target:
                return i

        return -1
