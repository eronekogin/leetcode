"""
https://leetcode.com/problems/count-of-interesting-subarrays/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def count_interesting_subarrays(self, nums: list[int], modulo: int, k: int) -> int:
        """
        count interesting subarrays
        """
        cnt = Counter([0])
        rslt = 0
        prefix = 0
        for x in nums:
            prefix += (x % modulo == k)
            rslt += cnt[(prefix - k + modulo) % modulo]
            cnt[prefix % modulo] += 1

        return rslt


print(Solution().count_interesting_subarrays([3, 2, 4], 2, 1))
