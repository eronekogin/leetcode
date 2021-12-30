"""
https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/
"""


from collections import defaultdict


class Solution:
    def sortItems(
        self,
        n: int,
        m: int,
        group: list[int],
        beforeItems: list[list[int]]
    ) -> list[int]:
        def get_topological_order(
            graph: list[list[int]],
            indgree: list[int]
        ) -> list[int]:
            rslt = []
            stack = [node for node in range(len(graph)) if indgree[node] == 0]
            while stack:
                src = stack.pop()
                rslt.append(src)
                for dst in graph[src]:
                    indgree[dst] -= 1
                    if indgree[dst] == 0:
                        stack.append(dst)

            if len(rslt) == len(graph):
                return rslt

            return []

        # Create a new group for each item that does not belong to any group.
        currGroup = m
        for node in range(len(group)):
            if group[node] == -1:
                group[node] = currGroup
                currGroup += 1

        # Build directed graph for items and groups.
        graphItems = [[] for _ in range(n)]
        indgreeItems = [0] * n
        graphGroups = [[] for _ in range(currGroup)]
        indgreeGroups = [0] * currGroup
        for dst in range(n):
            for src in beforeItems[dst]:
                graphItems[src].append(dst)
                indgreeItems[dst] += 1

                if group[src] != group[dst]:
                    graphGroups[group[src]].append(group[dst])
                    indgreeGroups[group[dst]] += 1

        # Sort items and groups.
        itemOrder = get_topological_order(graphItems, indgreeItems)
        groupOrder = get_topological_order(graphGroups, indgreeGroups)
        if not itemOrder or not groupOrder:
            return []

        # Sort all the items within each group.
        itemOrderPerGroup = defaultdict(list)
        for node in itemOrder:
            itemOrderPerGroup[group[node]].append(node)

        # Combine with group order.
        rslt = []
        for group in groupOrder:
            rslt.extend(itemOrderPerGroup[group])

        return rslt
