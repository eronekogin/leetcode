"""
https://leetcode.com/problems/seat-reservation-manager/
"""


from heapq import heappush, heappop, heapify


class SeatManager:

    def __init__(self, n: int):
        self.availableSeats = list(range(1, n + 1))
        heapify(self.availableSeats)

    def reserve(self) -> int:
        return heappop(self.availableSeats)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.availableSeats, seatNumber)
