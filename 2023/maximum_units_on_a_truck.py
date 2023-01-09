"""
https://leetcode.com/problems/maximum-units-on-a-truck/
"""


class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        sortedBoxes = sorted(boxTypes, key=lambda x: -x[1])
        totalUnits = 0
        currBoxes = 0
        for totalBox, unitPerBox in sortedBoxes:
            if currBoxes + totalBox < truckSize:
                currBoxes += totalBox
                totalUnits += totalBox * unitPerBox
            else:
                totalUnits += (truckSize - currBoxes) * unitPerBox
                break

        return totalUnits


print(Solution().maximumUnits([[1, 3], [2, 2], [3, 1]], 4))
