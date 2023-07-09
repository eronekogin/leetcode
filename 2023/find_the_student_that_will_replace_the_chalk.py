"""
https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/
"""


class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        oneRoundSum = sum(chalk)
        remain = k % oneRoundSum
        for i, usedChalk in enumerate(chalk):
            if remain < usedChalk:
                return i
            
            remain -= usedChalk
        
        return -1  # Not reachable.