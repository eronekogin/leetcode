"""
https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/
"""


from heapq import heappush, heappop, heapify


class Solution:
    def smallestChair(self, times: list[list[int]], targetFriend: int) -> int:
        N = len(times) + 1
        availableSeats = list(range(N))
        heapify(availableSeats)

        takenSeats = []

        sortedTimes = sorted([(i, arrival, leave) for i, (arrival, leave) in enumerate(times)], key=lambda x: x[1])

        for i, arrive, leave in sortedTimes:
            while takenSeats and takenSeats[0][0] <= arrive:
                _, seat = heappop(takenSeats)
                heappush(availableSeats, seat)
            
            currTakenSeat = heappop(availableSeats)
            if i == targetFriend:
                return currTakenSeat
            
            heappush(takenSeats, (leave, currTakenSeat))
        
        return -1  # Not possible.


print(Solution().smallestChair([[1,4],[2,3],[4,6]], 1))