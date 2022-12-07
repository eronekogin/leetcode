"""
https://leetcode.com/problems/count-of-matches-in-tournament/
"""


class Solution:
    def numberOfMatches(self, n: int) -> int:
        matchCnt = 0
        remainTeams = n
        while remainTeams > 1:
            isOdd = remainTeams & 1
            remainTeams = ((remainTeams - isOdd) >> 1) + isOdd
            matchCnt += remainTeams - isOdd

        return matchCnt


print(Solution().numberOfMatches(7))
