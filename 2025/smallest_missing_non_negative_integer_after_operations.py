"""
https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def find_smallest_integer(self, nums: list[int], value: int) -> int:
        """
        find smallest integer
        """
        cnt = Counter(x % value for x in nums)
        min_index, min_freqs = 0, len(nums) + 1
        for i in range(value):
            if i not in cnt:
                return i

            if cnt[i] < min_freqs:
                min_freqs = cnt[i]
                min_index = i

        return min_freqs * value + min_index


print(Solution().find_smallest_integer([3, 0, 3, 2, 4, 2, 1, 1, 0, 4], 5))
