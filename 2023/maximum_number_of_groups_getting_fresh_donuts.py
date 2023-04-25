"""
https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/
"""


from functools import cache


class Solution:
    def maxHappyGroups(self, batchSize: int, groups: list[int]) -> int:
        @cache
        def dfs(currPositions: tuple[int], currNumber: int):
            if sum(currPositions) == 0:
                return 0

            rslt = -1
            for i in range(batchSize):
                if currPositions[i] > 0:
                    nextPositions = list(currPositions)
                    nextPositions[i] -= 1
                    nextNumber = (currNumber - i) % batchSize
                    rslt = max(
                        rslt,
                        dfs(tuple(nextPositions), nextNumber) +
                        (nextNumber == 0)
                    )

            return rslt

        # Count always happy group first.
        rslt, remainGroups, positions = 0, [], [0] * batchSize
        for group in groups:
            i = group % batchSize
            if i > 0:
                remainGroups.append(group)
                positions[i] += 1
            else:
                rslt += 1

        # Then combine the remain groups having
        # group[i] + group[j] == batchSize, those pair group can form
        # happy groups if being put adjancent.
        for i in range(1, batchSize):
            if (i << 1) != batchSize:
                pairs = min(positions[i], positions[batchSize - i])
            else:
                pairs = positions[i] >> 1

            rslt += pairs
            positions[i] -= pairs
            positions[batchSize - i] -= pairs

        if sum(positions) == 0:  # All paird up.
            return rslt

        # Still having unpaird groups, using dfs to get the maximum happy
        # groups.
        return max(
            dfs(tuple(positions), i)
            for i in range(1, batchSize)
        ) + rslt
