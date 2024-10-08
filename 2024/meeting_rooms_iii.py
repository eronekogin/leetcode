"""
https://leetcode.com/problems/meeting-rooms-iii/description/
"""


from heapq import heapify, heappop, heappush


class Solution:
    """
    Solution
    """

    def most_booked(self, n: int, meetings: list[list[int]]) -> int:
        """
        most booked
        """
        cnt = [0] * n
        unused_rooms = list(range(n))
        used_rooms = []
        heapify(unused_rooms)

        for start, end in sorted(meetings):
            while used_rooms and used_rooms[0][0] <= start:
                _, room = heappop(used_rooms)
                heappush(unused_rooms, room)

            if unused_rooms:
                room = heappop(unused_rooms)
                heappush(used_rooms, (end, room))
            else:
                available, room = heappop(used_rooms)
                heappush(used_rooms, (available + end - start, room))

            cnt[room] += 1

        return cnt.index(max(cnt))


print(Solution().most_booked(
    4, [[18, 19], [3, 12], [17, 19], [2, 13], [7, 10]]))
