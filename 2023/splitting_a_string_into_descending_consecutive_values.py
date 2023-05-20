"""
https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/
"""


class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(start: int, currSize: int, prevNum: int, currSplits: int):
            if start == N and currSplits >= 2:
                return True

            while start + currSize <= N:
                currNum = int(s[start: start + currSize])
                currSize += 1

                if prevNum != -1 and currNum != prevNum - 1:
                    continue

                if dfs(start + currSize - 1, 1, currNum, currSplits + 1):
                    return True

            return False

        N = len(s)
        return dfs(0, 1, -1, 0)
