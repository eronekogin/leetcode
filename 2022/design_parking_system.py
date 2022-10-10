"""
https://leetcode.com/problems/design-parking-system/
"""


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.capacity = [None, big, medium, small]

    def addCar(self, carType: int) -> bool:
        if not self.capacity[carType]:
            return False

        self.capacity[carType] -= 1
        return True
