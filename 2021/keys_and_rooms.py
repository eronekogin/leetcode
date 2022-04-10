"""
https://leetcode.com/problems/keys-and-rooms/
"""


class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = set()
        currRooms = {0}
        while currRooms:
            nextRooms = set()
            for currRoom in currRooms:
                if currRoom not in visited:
                    visited.add(currRoom)
                    nextRooms |= set(rooms[currRoom])

            currRooms = nextRooms

        return len(visited) == len(rooms)


print(Solution().canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))
