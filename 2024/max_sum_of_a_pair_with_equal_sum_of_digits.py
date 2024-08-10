"""
https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/description/
"""


from collections import defaultdict


class Solution:
    """
    Solution
    """

    def maximum_sum(self, nums: list[int]) -> int:
        """
        maximum sum
        """
        def sum_digits(x: int):
            rslt = 0
            while x:
                x, r = divmod(x, 10)
                rslt += r

            return rslt

        memo: defaultdict[int, list[int]] = defaultdict(list)
        for x in nums:
            memo[sum_digits(x)].append(x)

        max_sum = -1
        for v in memo.values():
            if len(v) < 2:
                continue

            max_sum = max(
                max_sum,
                sum(sorted(v, reverse=True)[:2])
            )

        return max_sum


print(Solution().maximum_sum([368, 369, 307, 304, 384, 138, 90,
      279, 35, 396, 114, 328, 251, 364, 300, 191, 438, 467, 183]))
