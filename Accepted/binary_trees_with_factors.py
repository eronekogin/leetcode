"""
https://leetcode.com/problems/binary-trees-with-factors/
"""


class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        """
        1. Suppose dp[i] stands for the number of ways to make a binary tree
            with root node as arr[i], then we have:
            dp[i] = sum(dp[x] * dp[y] if x * y == i)
        2. Optimizations:
            2.1 We sort the input list in ascending order so that we could
                only consider building the target dp[i] with numbers before
                the ith number.
            2.2 We consider the case x <= y:
                2.2.1 If x < y, the result will be 2 * dp[x] * dp[y] since
                    left tree and right tree are considered different trees.
                2.2.2 If x == y, the result will be dp[x] * dp[y] since
                    exchanging left and right makes no difference.
        """
        dp = {}
        for num in sorted(arr):
            dp[num] = 1
            for x in dp:
                y, r = divmod(num, x)
                if y < x:  # No need to loop any longer.
                    break

                if not r and y in dp:
                    if x == y:
                        dp[num] += dp[x] ** 2
                    else:
                        dp[num] += (dp[x] * dp[y]) << 1

        return sum(dp.values()) % (10 ** 9 + 7)
