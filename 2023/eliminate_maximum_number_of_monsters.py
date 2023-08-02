"""
https://leetcode.com/problems/eliminate-maximum-number-of-monsters/
"""


class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        for readyTime, arrivalTime in enumerate(sorted((d - 1) // s for d, s in zip(dist, speed))):
            if readyTime > arrivalTime:
                return readyTime
        
        return len(dist)


print(Solution().eliminateMaximum([4,2,3], [2,1,1]))