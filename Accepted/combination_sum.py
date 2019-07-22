"""
https://leetcode.com/problems/combination-sum/
"""

from typing import List


class Solution:
    def combinationSum(
            self, candidates: List[int], target: int) -> List[List[int]]:

        def sub_sum(remain: int, path: List[int], start: int) -> None:
            if remain == 0:  # Combination found.
                rsltList.append(path)
                return

            for i in range(start, len(workList)):
                if workList[i] > remain:  # Exceed when adding workList[i]
                    break

                sub_sum(remain - workList[i], path + [workList[i]], i)

        workList = sorted(candidates)  # Avoid duplicates.
        rsltList = []
        sub_sum(target, [], 0)
        return rsltList


candidates, target = [2, 3, 5], 8
print(Solution().combinationSum(candidates, target))
