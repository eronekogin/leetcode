"""
https://leetcode.com/problems/rearranging-fruits/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def min_cost(self, basket1: list[int], basket2: list[int]) -> int:
        """
        Two ways of swap:

        1. Swap number at the current index
        2. Swap number with the smallest number, then swap the smallest number back.

        See /pics/pics/two-way-swap.png for more details.
        """
        cnt = Counter(basket1 + basket2)
        for k, v in cnt.items():
            if v & 1:
                return -1

            cnt[k] >>= 1

        diff1 = list((Counter(basket1) - cnt).elements())
        diff2 = list((Counter(basket2) - cnt).elements())
        min_num = min(cnt.keys())
        diffs = sorted(diff1 + diff2)

        return sum(
            min(min_num << 1, diffs[i])
            for i in range(len(diff1))
        )


print(Solution().min_cost(
    [84, 80, 43, 8, 80, 88, 43, 14, 100, 88],
    [32, 32, 42, 68, 68, 100, 42, 84, 14, 8]
))
