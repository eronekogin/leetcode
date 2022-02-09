"""
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        totalProduct, totalSum = 1, 0
        while n:
            n, d = divmod(n, 10)
            totalProduct *= d
            totalSum += d

        return totalProduct - totalSum


print(Solution().subtractProductAndSum(234))
