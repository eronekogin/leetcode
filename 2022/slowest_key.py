"""
https://leetcode.com/problems/slowest-key/
"""


class Solution:
    def slowestKey(self, releaseTimes: list[int], keysPressed: str) -> str:
        durations = [0] * 26
        BASE = ord('a')
        for i, c in enumerate(keysPressed):
            offset = ord(c) - BASE
            if i < 1:
                durations[offset] = releaseTimes[i]
            else:
                durations[offset] = max(
                    durations[offset],
                    releaseTimes[i] - releaseTimes[i - 1]
                )

        maxDuration = 0
        maxChar = 'a'
        for i, duration in enumerate(durations):
            if duration >= maxDuration:
                maxDuration = duration
                maxChar = chr(i + BASE)

        return maxChar


print(Solution().slowestKey([19, 22, 28, 29, 66, 81, 93, 97],
                            "fnfaaxha"))
