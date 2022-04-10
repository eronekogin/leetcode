"""
https://leetcode.com/problems/max-number-of-k-sum-pairs/
"""


from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        opCnt, memo = 0, {}
        for num in nums:
            p = k - num
            if p in memo:
                opCnt += 1
                memo[p] -= 1
                if not memo[p]:
                    del memo[p]
            else:
                memo[num] = memo.get(num, 0) + 1

        return opCnt


print(Solution().maxOperations([3, 1, 3, 4, 3], 6))
