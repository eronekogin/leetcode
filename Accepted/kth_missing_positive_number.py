"""
https://leetcode.com/problems/kth-missing-positive-number/
"""


from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missingNum, missingCnt = 1, 0
        for num in arr:
            while num > missingNum:
                missingCnt += 1
                if missingCnt == k:
                    return missingNum

                missingNum += 1

            missingNum += 1

        return missingNum - 1 + k - missingCnt


print(Solution().findKthPositive([1, 2, 4], 3))
