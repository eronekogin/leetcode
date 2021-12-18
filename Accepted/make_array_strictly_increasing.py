"""
https://leetcode.com/problems/make-array-strictly-increasing/
"""


from collections import defaultdict
from bisect import bisect_right


class Solution:
    def makeArrayIncreasing(self, arr1: list[int], arr2: list[int]) -> int:
        currDp: dict[int, int] = {-1: 0}  # {index: number of operations}
        sortedList = sorted(arr2)
        N = len(sortedList)
        for num1 in arr1:
            nextDp = defaultdict(lambda: float('inf'))
            for num2 in currDp:
                if num1 > num2:
                    nextDp[num1] = min(nextDp[num1], currDp[num2])

                i2 = bisect_right(sortedList, num2)
                if i2 < N:
                    nextDp[sortedList[i2]] = min(
                        nextDp[sortedList[i2]], currDp[num2] + 1)

            currDp = nextDp

        if currDp:
            return min(currDp.values())

        return -1  # Not able to make arr1 strictly ascending.
