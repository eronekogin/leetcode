"""
https://leetcode.com/problems/avoid-flood-in-the-city/
"""


from heapq import heappush, heappop
from collections import defaultdict, deque


class Solution:
    def avoidFlood(self, rains: list[int]) -> list[int]:
        N = len(rains)
        rainingDays = defaultdict(deque)
        rslt = [-1] * N
        heap = []
        fullLakes = set()

        # Collect raining days.
        for day, lake in enumerate(rains):
            rainingDays[lake].append(day)

        # Compose dry solutions.
        for day, lake in enumerate(rains):
            if lake > 0:  # Has rain today.
                if lake in fullLakes:
                    return []  # Not possible.

                fullLakes.add(lake)

                # Keep pop out days that are deprecated.
                while rainingDays[lake] and rainingDays[lake][0] <= day:
                    rainingDays[lake].popleft()

                if rainingDays[lake]:
                    heappush(heap, rainingDays[lake][0])
            else:  # Has no rain today.
                if heap:
                    # Dry the most urgent full lake, in other words, the lake
                    # which will be rained in the nearest future.
                    rslt[day] = rains[heappop(heap)]
                    fullLakes.remove(rslt[day])
                else:
                    # Nothing to dry, by default dry on the first lake.
                    rslt[day] = 1

        return rslt


print(Solution().avoidFlood([69, 0, 0, 0, 69]))
