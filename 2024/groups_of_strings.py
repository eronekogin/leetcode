"""
https://leetcode.com/problems/groups-of-strings/description/
"""


from collections import defaultdict


class Solution:
    """
    Solution
    """

    def group_strings(self, words: list[str]) -> list[int]:
        """
        group_strings
        """
        # generate replace mask such that a*cd pattern will
        # have the same masks, such as abcd, aecd, afcd, ...
        offset = ord('a')
        star_mask = 1 << 26
        initial_masks = {
            sum(
                1 << (ord(c) - offset)
                for c in w
            ): i
            for i, w in enumerate(words)
        }

        graph: defaultdict[int, list[int]] = defaultdict(list)
        masks: defaultdict[int, list[int]] = defaultdict(list)
        for i, w in enumerate(words):
            values = [ord(c) - offset for c in w]
            curr_mask = sum(1 << v for v in values)

            for v in values:
                # take * inside a*cd pattern as 1<<26 and calculate
                # its mask as a replace mask.
                masks[curr_mask - (1 << v) + star_mask].append(i)

                remove_mask = curr_mask - (1 << v)

                if remove_mask not in initial_masks:
                    continue

                j = initial_masks[remove_mask]

                # i and j are connected in graph.
                graph[i].append(j)
                graph[j].append(i)

        for x in masks.values():
            for i, j in zip(x, x[1:]):
                graph[i].append(j)
                graph[j].append(i)

        visited = set()
        max_group_size = 0
        max_groups = 0
        for u in range(len(words)):
            if u in visited:
                continue

            curr_group_size = 1
            queue = [u]
            visited.add(u)
            while queue:
                x = queue.pop()
                for v in graph[x]:
                    if v in visited:
                        continue

                    curr_group_size += 1
                    visited.add(v)
                    queue.append(v)

            max_group_size = max(max_group_size, curr_group_size)
            max_groups += 1

        return [max_groups, max_group_size]
