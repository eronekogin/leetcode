"""
https://leetcode.com/problems/longest-harmonious-subsequence/
"""


from typing import List


from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        memo = {}
        rslt = 0
        for num in nums:
            memo[num] = memo.get(num, 0) + 1
            if num + 1 in memo:
                rslt = max(rslt, memo[num + 1] + memo[num])

            if num - 1 in memo:
                rslt = max(rslt, memo[num - 1] + memo[num])

        return rslt

    def findLHS2(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return max([cnt[k] + cnt[k + 1] for k in cnt if k + 1 in cnt] or [0])


print(Solution().findLHS([1, 3, 2, 2, 5, 2, 3, 7]))
