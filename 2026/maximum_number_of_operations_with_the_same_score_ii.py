"""
https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/description/
"""


class Solution:
    """
    Solution
    """

    def max_operations(self, nums: list[int]) -> int:
        """
        max operations
        """
        def get_ops(l: int, r: int, target: int) -> int:
            if l >= r:
                return 0

            if memo[l][r]:
                return memo[l][r]

            max_ops = 0
            if nums[l] + nums[l + 1] == target:
                max_ops = max(
                    max_ops,
                    1 + get_ops(l + 2, r, target)
                )

            if nums[l] + nums[r] == target:
                max_ops = max(
                    max_ops,
                    1 + get_ops(l + 1, r - 1, target)
                )

            if nums[r] + nums[r - 1] == target:
                max_ops = max(
                    max_ops,
                    1 + get_ops(l, r - 2, target)
                )

            memo[l][r] = max_ops
            return max_ops

        n = len(nums)
        memo = [[0] * n for _ in range(n)]
        return max(
            get_ops(2, n - 1, nums[0] + nums[1]),
            get_ops(1, n - 2, nums[0] + nums[-1]),
            get_ops(0, n - 3, nums[-1] + nums[-2])
        ) + 1


print(Solution().max_operations([1, 9, 7, 3, 2, 7, 4, 12, 2, 6]))
