"""
https://leetcode.com/problems/maximum-strength-of-k-disjoint-subarrays/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_strength(self, nums: list[int], k: int) -> int:
        """
        In the final solution, all the disjoint subarrays are continous.
        For example, if k=3, we choose 3 disjoint subarrays a, b, c
        result = 3*sum(a) - 2*sum(b) + sum(c)
        If there is a subarray d between a and b, then d can be combined to a to increase sum(a) or combined to b to decrease sum(b)

        Therefore, for each index i, index i+1 either in current subarray or in next subarray
        """
        n = len(nums)
        dp = [0] * (n + 1)

        for i in range(1, k + 1):
            prev = dp.copy()
            for j in range(n - 1, -1, -1):
                dp[j] = (
                    nums[j] * i * (-1) ** (k - i) +
                    max(dp[j + 1], prev[j + 1])
                )

            dp[n - i + 1] = -float('inf')

        return max(dp)
