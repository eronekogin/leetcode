"""
https://leetcode.com/problems/destroy-sequential-targets/description/
"""


from collections import defaultdict


class Solution:
    """
    Solution
    """

    def destroy_targets(self, nums: list[int], space: int) -> int:
        """
        destroy targets
        """
        memo = defaultdict(list)

        for x in nums:
            memo[x % space].append(x)

        max_len = 0
        min_val = 10 ** 6
        for v in memo.values():
            if len(v) > max_len:
                max_len = len(v)
                min_val = min(v)
            elif len(v) == max_len and min(v) < min_val:
                min_val = min(v)

        return min_val


print(Solution().destroy_targets([1, 3, 5, 2, 4, 6], 2))
