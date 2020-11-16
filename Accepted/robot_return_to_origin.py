"""
https://leetcode.com/problems/robot-return-to-origin/
"""


from collections import Counter


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cnt = Counter(moves)
        return cnt['U'] == cnt['D'] and cnt['L'] == cnt['R']
