"""
https://leetcode.com/problems/array-of-doubled-pairs/
"""


from collections import Counter


class Solution:
    def canReorderDoubled(self, arr: list[int]) -> bool:
        memo = Counter(arr)
        for x in sorted(memo, key=abs):
            if memo[x << 1] < memo[x]:
                return False
            else:
                memo[x << 1] -= memo[x]

        return True


print(Solution().canReorderDoubled([1, 2, 4, 16, 8, 4]))
