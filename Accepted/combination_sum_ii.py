"""
https://leetcode.com/problems/combination-sum-ii/
"""

from typing import List


class Solution:
    def combinationSum2(
            self, candidates: List[int], target: int) -> List[List[int]]:

        def sub_sum(remain: int, path: List[int], start: int) -> None:
            if remain == 0:  # Combination found.
                rsltList.append(path)
                return

            for i in range(start, len(workList)):
                # We don't need to walk through the same sequence
                # again which was traversed in the previous rounds.
                if i > start and workList[i] == workList[i - 1]:
                    continue  # Avoid duplicates.

                if workList[i] > remain:  # Exceed when adding workList[i].
                    break

                sub_sum(remain - workList[i], path + [workList[i]], i + 1)

        workList = sorted(candidates)  # Avoid duplicates.
        rsltList = []
        sub_sum(target, [], 0)
        return rsltList


candidates, target = [3, 1, 3, 5, 1, 1], 8
print(Solution().combinationSum2(candidates, target))
