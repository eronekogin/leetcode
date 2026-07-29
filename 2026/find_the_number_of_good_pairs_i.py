"""
https://leetcode.com/problems/find-the-number-of-good-pairs-i/description/
"""


class Solution:
    """
    Solution
    """

    def number_of_pairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        """
        number of pairs
        """
        total_pairs = 0
        memo = {}
        for x in nums1:
            if x in memo:
                total_pairs += memo[x]
                continue

            curr_pairs = 0
            for y in nums2:
                if x % (k * y) == 0:
                    curr_pairs += 1

            memo[x] = curr_pairs
            total_pairs += curr_pairs

        return total_pairs


print(Solution().number_of_pairs([1, 3, 4], [1, 3, 4], 1))
