"""
https://leetcode.com/problems/time-needed-to-inform-all-employees/
"""


from collections import defaultdict


class Solution:
    def numOfMinutes(
        self,
        n: int,
        headID: int,
        manager: list[int],
        informTime: list[int]
    ) -> int:
        def notify(managerId: int) -> int:
            maxTime = max(
                [
                    notify(employeeId)
                    for employeeId in employeeMap[managerId]
                ] or
                [0]
            )
            return maxTime + informTime[managerId]

        # Build map.
        employeeMap = defaultdict(list)
        for i, m in enumerate(manager):
            employeeMap[m].append(i)

        return notify(headID)


print(Solution().numOfMinutes(11,
                              4,
                              [5, 9, 6, 10, -1, 8, 9, 1, 9, 3, 4],
                              [0, 213, 0, 253, 686, 170, 975, 0, 261, 309, 337]))
