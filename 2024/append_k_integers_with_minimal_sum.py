"""
https://leetcode.com/problems/append-k-integers-with-minimal-sum/description/
"""


class Solution:
    """
    Solution
    """

    def minimal_k_sum(self, nums: list[int], k: int) -> int:
        """
        minimum k sum
        """
        min_sum = (k * (k + 1)) >> 1
        curr_max = k + 1
        for x in sorted(set(nums)):
            if x < curr_max:
                min_sum += curr_max - x
                curr_max += 1

        return min_sum


print(Solution().minimal_k_sum([93, 44, 49, 45, 93, 52, 6, 7, 88, 70, 86, 15, 38, 86, 86, 95, 8,
      62, 13, 84, 26, 16, 33, 85, 7, 62, 55, 50, 77, 10, 76, 10, 35, 67, 19, 12, 24, 39, 76, 37], 17))
