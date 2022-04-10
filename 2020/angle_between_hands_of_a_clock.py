"""
https://leetcode.com/problems/angle-between-hands-of-a-clock/
"""


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        ANGLE_PER_HOUR, ANGLE_PER_MIN = 30, 6  # 360/12, 360/6.
        currMinuteAngle = minutes * ANGLE_PER_MIN
        currHourAngle = (hour % 12 + minutes / 60) * ANGLE_PER_HOUR
        candidateAngle = abs(currHourAngle - currMinuteAngle)
        return min(candidateAngle, 360 - candidateAngle)


print(Solution().angleClock(12, 30))
