"""
https://leetcode.com/problems/find-all-people-with-secret/
"""


from itertools import groupby
from collections import defaultdict, deque


class Solution:
    """
    Solution
    """

    def find_all_people(
        self,
        n: int,
        meetings: list[list[int]],
        first_person: int
    ) -> list[int]:
        """
        find_all_people
        """
        candidates = {0, first_person}
        for _, grp in groupby(sorted(meetings, key=lambda x: x[2]), key=lambda x: x[2]):
            queue = set()
            graph = defaultdict(list)
            for x, y, _ in grp:
                graph[x].append(y)
                graph[y].append(x)
                if x in candidates:
                    queue.add(x)

                if y in candidates:
                    queue.add(y)

            queue = deque(queue)
            while queue:
                x = queue.popleft()
                for y in graph[x]:
                    if y not in candidates:
                        candidates.add(y)
                        queue.append(y)

        return list(candidates)
