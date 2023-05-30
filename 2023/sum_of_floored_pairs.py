"""
https://leetcode.com/problems/sum-of-floored-pairs/
"""


from collections import Counter
from itertools import accumulate


class Solution:
    def sumOfFlooredPairs(self, nums: list[int]) -> int:
        incs = [0] * (max(nums) + 1)
        cnt = Counter(nums)

        for num in cnt:
            for j in range(num, len(incs), num):
                incs[j] += cnt[num]

        quotients = list(accumulate(incs))
        return sum(quotients[num] for num in nums) % (10 ** 9 + 7)
