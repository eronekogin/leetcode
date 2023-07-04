"""
https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/
"""


from collections import Counter
from itertools import accumulate


class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        cnt = Counter(nums)
        sortedKeys = sorted(cnt, reverse=True)
        sortedValues = [cnt[k] for k in sortedKeys]
        return sum(list(accumulate(sortedValues))[:-1])


print(Solution().reductionOperations([5,3,1]))

