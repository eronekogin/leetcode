"""
https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/
"""


class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        def get_minutes(time: str):
            hh, mm = (int(x) for x in time.split(':'))
            return hh * 60 + mm
        
        startTime, endTime = get_minutes(loginTime), get_minutes(logoutTime)
        

        """
        endTime // 15 stands for the same or less endTime for the previous round.

        (startTime + 14) // 15 stands for the same or less startTime for the previous round.

        and if startTime >= endTime, we add a full day rounds to the result to indicate over midnight.
        """
        return max(
            0,
            endTime // 15 - (startTime + 14) // 15 + (startTime >= endTime) * 4 * 24
        )


print(Solution().numberOfRounds('21:30', '03:00'))