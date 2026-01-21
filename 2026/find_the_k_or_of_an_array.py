"""
https://leetcode.com/problems/find-the-k-or-of-an-array/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def find_k_or(self, nums: list[int], k: int) -> int:
        """
        Docstring for find_k_or

        :param self: Description
        :param nums: Description
        :type nums: list[int]
        :param k: Description
        :type k: int
        :return: Description
        :rtype: int
        """
        bit_counts = [0] * 32
        for x in nums:
            for i in range(32):
                if x & (1 << i):
                    bit_counts[i] += 1

        rslt = 0
        for x in reversed(bit_counts):
            rslt = rslt * 2 + (x >= k)

        return rslt


print(Solution().find_k_or([7, 12, 9, 8, 9, 15], 4))
