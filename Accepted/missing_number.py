"""
https://leetcode.com/problems/missing-number/
"""


from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        n is replacing the missing number from range [0, n - 1],
        so xor the index and the actual value will eventually get us
        the n ^ k, where k is the missing number. Then we could simply
        do a (n ^ k) ^ n to get the target k.
        """
        rslt = len(nums)
        for i, num in enumerate(nums):
            rslt ^= i ^ num

        return rslt

    def missingNumber2(self, nums: List[int]) -> int:
        """
        Math: the total sum from 0 to n is (1 + n) * n // 2.
        Then the total sum - sum of nums will get us the missing number.
        """
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)


print(Solution().missingNumber([1, 2]))
