"""
https://leetcode.com/problems/groups-of-special-equivalent-strings/
"""


class Solution:
    def numSpecialEquivGroups(self, words: list[str]) -> int:
        return len({tuple(sorted(w[0::2]) + sorted(w[1::2])) for w in words})
