"""
https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
"""


class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        sortedGroupSizes = sorted(
            (size, i)
            for i, size in enumerate(groupSizes)
        )
        groups = []
        preSize = None
        for currSize, i in sortedGroupSizes:
            if preSize != currSize or (groups and len(groups[-1]) == currSize):
                # Open a new group to hold more people.
                groups.append([])
                preSize = currSize

            # Add the current person to group.
            groups[-1].append(i)

        return groups


print(Solution().groupThePeople([3, 3, 3, 3, 3, 1, 3]))
