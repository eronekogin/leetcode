"""
https://leetcode.com/problems/design-underground-system/
"""


class UndergroundSystem:

    def __init__(self):
        self._lastCheckIn = {}  # {userId: [startStation, time]}
        self._memo = {}  # {(startStation, endStation): (total, cnt)}

    def checkIn(self, userId: int, stationName: str, t: int) -> None:
        if userId not in self._lastCheckIn:
            self._lastCheckIn[userId] = [None, None]

        self._lastCheckIn[userId][0] = stationName
        self._lastCheckIn[userId][1] = t

    def checkOut(self, userId: int, stationName: str, t: int) -> None:
        startStation, startTime = self._lastCheckIn[userId]
        if (startStation, stationName) not in self._memo:
            self._memo[(startStation, stationName)] = [0, 0]

        total, cnt = self._memo[(startStation, stationName)]
        self._memo[(startStation, stationName)][0] = total + t - startTime
        self._memo[(startStation, stationName)][1] = cnt + 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, cnt = self._memo[(startStation, endStation)]
        return total / cnt


undergroundSystem = UndergroundSystem()
undergroundSystem.checkIn(10, "Leyton", 3)
undergroundSystem.checkOut(10, "Paradise", 8)
undergroundSystem.getAverageTime("Leyton", "Paradise")
undergroundSystem.checkIn(5, "Leyton", 10)
undergroundSystem.checkOut(5, "Paradise", 16)
undergroundSystem.getAverageTime("Leyton", "Paradise")
undergroundSystem.checkIn(2, "Leyton", 21)
undergroundSystem.checkOut(2, "Paradise", 30)
undergroundSystem.getAverageTime("Leyton", "Paradise")
