"""
https://leetcode.com/problems/delete-and-earn/
"""


from typing import List


from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        1. If we take one number, we should take all its duplicates as well
            since if we remove all its neighbors the first time, there is no
            additional change for the remaining remove times.
        2. If we sort all the unique numbers in the list in ascending order,
            we could simply compare the latest number with its previous number
            to check if they are adjancent or not. Then apply dp against both
            cases.
        """
        pointsWithCurrNum, pointsWithoutCurrNum, prev = 0, 0, None
        cnt = Counter(nums)
        for curr in sorted(cnt):
            if curr - 1 != prev:  # curr is not adjancent to prev.
                pointsWithoutCurrNum, pointsWithCurrNum = (
                    max(pointsWithCurrNum, pointsWithoutCurrNum),
                    curr * cnt[curr] + max(
                        pointsWithCurrNum, pointsWithoutCurrNum))
            else:  # curr is adjancent to prev.
                pointsWithoutCurrNum, pointsWithCurrNum = (
                    max(pointsWithCurrNum, pointsWithoutCurrNum),
                    curr * cnt[curr] + pointsWithoutCurrNum)

            prev = curr

        return max(pointsWithCurrNum, pointsWithoutCurrNum)


print(Solution().deleteAndEarn([3, 4, 2]))
