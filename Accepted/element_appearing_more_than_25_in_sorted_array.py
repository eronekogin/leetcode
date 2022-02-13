"""
https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
"""


class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        minCnt = len(arr) / 4
        preNum = None
        cnt = 0
        for num in arr:
            if num != preNum:
                if cnt > minCnt:
                    break

                preNum = num
                cnt = 0

            cnt += 1

        return preNum


print(Solution().findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10]))
