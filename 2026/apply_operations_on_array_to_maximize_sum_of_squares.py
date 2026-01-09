"""
https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def max_sum(self, nums: list[int], k: int) -> int:
        """
        Consider 4 cases for each bit of nums[i] and nums[j]:

            (1, 0) -> (0, 1)
            (0, 1) -> (0, 1)
            (1, 1) -> (1, 1)
            (0, 0) -> (0, 0)

        So only the first case will move the 1 from nums[i] to
        nums[j], the remaining cases won't change anything after
        one operation
        """
        max_bit = 32
        bit_freqs = [0] * max_bit
        for x in nums:
            for i in range(max_bit):
                if x & (1 << i):
                    bit_freqs[i] += 1

        rslt = 0
        m = 10 ** 9 + 7
        for _ in range(k):
            x = 0
            for i in range(max_bit):
                if bit_freqs[i]:
                    bit_freqs[i] -= 1
                    x += 1 << i

            rslt += x * x % m

        return rslt % m
