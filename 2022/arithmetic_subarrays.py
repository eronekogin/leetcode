"""
https://leetcode.com/problems/arithmetic-subarrays/
"""


class Solution:
    def checkArithmeticSubarrays(
        self,
        nums: list[int],
        l: list[int],
        r: list[int]
    ) -> list[bool]:
        rslt: list[bool] = []
        for start, end in zip(l, r):
            if end - start + 1 < 2:
                rslt.append(False)
            else:
                items = sorted(nums[start: end + 1])
                diff = items[1] - items[0]
                rslt.append(
                    all(y == x + diff for x, y in zip(items, items[1:]))
                )

        return rslt
