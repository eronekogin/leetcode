"""
https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/description/
"""


class Solution:
    """
    Solution
    """

    def sum_digit_differences(self, nums: list[int]) -> int:
        """
        sum digit differences
        """
        n = len(nums)
        m = len(str(nums[0]))
        cnt = [[0] * 10 for _ in range(m)]

        # When every digit is different in every position in
        # every pair.
        total = n * (n - 1) // 2 * m

        for x in nums:
            i = 0
            while x:
                x, r = divmod(x, 10)
                total -= cnt[i][r]
                cnt[i][r] += 1
                i += 1

        return total
