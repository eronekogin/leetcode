"""
https://leetcode.com/problems/count-unhappy-friends/
"""


class Solution:
    def unhappyFriends(
        self,
        n: int,
        preferences: list[list[int]],
        pairs: list[list[int]]
    ) -> int:
        pairMemo: dict[int, set[int]] = {}
        for x, y in pairs:
            pairMemo[x] = set(preferences[x][:preferences[x].index(y)])
            pairMemo[y] = set(preferences[y][:preferences[y].index(x)])

        unhappys = 0
        for x in pairMemo:
            for y in pairMemo[x]:
                if x in pairMemo[y]:
                    unhappys += 1
                    break

        return unhappys
