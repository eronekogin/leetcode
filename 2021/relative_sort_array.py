"""
https://leetcode.com/problems/relative-sort-array/
"""


from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        memoBoth, memoArr1 = Counter(), Counter()
        checks = set(arr2)
        for num in arr1:
            if num in checks:
                memoBoth[num] += 1
            else:
                memoArr1[num] += 1

        rslt = []
        for num in arr2:
            rslt.extend([num] * memoBoth[num])

        for num in sorted(memoArr1):
            rslt.extend([num] * memoArr1[num])

        return rslt
