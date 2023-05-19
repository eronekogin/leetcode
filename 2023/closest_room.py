"""
https://leetcode.com/problems/closest-room/
"""

from bisect import bisect_right, insort_right


class Solution:
    def closestRoom(self, rooms: list[list[int]], queries: list[list[int]]) -> list[int]:
        def search_closet_room_id(preferId: int):
            if not roomIdsSoFar:  # Cannot reach the min size requirement
                return -1

            candidates = []
            i = bisect_right(roomIdsSoFar, preferId)
            if i > 0:
                candidates.append(roomIdsSoFar[i - 1])

            if i < len(roomIdsSoFar):
                candidates.append(roomIdsSoFar[i])

            return min(
                candidates,
                key=lambda x: abs(x - preferId)
            )

        roomIdsSoFar = []
        sortedRooms = sorted(rooms, key=lambda x: x[1], reverse=True)
        sortedQueries = sorted(
            [[i, q] for i, q in enumerate(queries)],
            key=lambda x: x[1][1],
            reverse=True
        )
        n, k = len(rooms), len(queries)
        i = 0
        rslt = [-1] * k

        for iq, (preferId, minSize) in sortedQueries:
            while i < n and sortedRooms[i][1] >= minSize:
                insort_right(roomIdsSoFar, sortedRooms[i][0])
                i += 1

            rslt[iq] = search_closet_room_id(preferId)

        return rslt
