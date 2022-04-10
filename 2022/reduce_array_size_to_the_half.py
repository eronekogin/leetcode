"""
https://leetcode.com/problems/reduce-array-size-to-the-half/
"""


from collections import Counter


class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        cnt = Counter(arr)
        freqs = sorted(cnt.values(), key=lambda x: -x)
        N = len(arr) >> 1
        totalRemovedNums = 0
        for i, freq in enumerate(freqs):
            if totalRemovedNums + freq < N:
                totalRemovedNums += freq
            else:
                return i + 1


print(Solution().minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))
