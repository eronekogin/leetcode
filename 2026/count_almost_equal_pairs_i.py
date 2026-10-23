"""
https://leetcode.com/problems/count-almost-equal-pairs-i/description/
"""


from collections import defaultdict
from itertools import combinations


class Solution:
    """
    Solution
    """
    def count_pairs(self, nums: list[int]) -> int:
        """
        count pairs
        """
        memo = defaultdict(list)
        pairs = 0

        max_digits = len(str(max(nums)))
        t_nums = [str(x).rjust(max_digits, '0') for x in nums]

        for x in t_nums:
            memo[''.join(sorted(x))].append(x)

        for v in memo.values():
            for s1, s2 in combinations(v, 2):
                if sum(c1 != c2 for c1, c2 in zip(s1, s2)) < 3:
                    pairs += 1

        return pairs
