"""
https://leetcode.com/problems/count-almost-equal-pairs-ii/description/
"""

from itertools import combinations_with_replacement


class Solution:
    """
    Solution
    """
    def count_pairs(self, nums: list[int]) -> int:
        """
        count pairs
        """
        def neighbors(x: int):
            chars = list(str(x))
            n = len(chars)
            transferred: set[int] = set()

            for i, j in combinations_with_replacement(range(n), 2):
                chars[i], chars[j] = chars[j], chars[i]

                for k, l in combinations_with_replacement(range(n), 2):
                    chars[k], chars[l] = chars[l], chars[k]

                    transferred.add(int(''.join(chars)))

                    chars[k], chars[l] = chars[l], chars[k]

                chars[i], chars[j] = chars[j], chars[i]

            return transferred

        pairs = 0
        cnt: dict[int, int] = {}
        for x in sorted(nums, reverse=True):
            pairs += cnt.get(x, 0)

            for y in neighbors(x):
                cnt[y] = cnt.get(y, 0) + 1

        return pairs
