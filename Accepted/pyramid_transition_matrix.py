"""
https://leetcode.com/problems/pyramid-transition-matrix/
"""


from typing import List


from collections import defaultdict

from itertools import product


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        def solve(currBottom: str) -> bool:
            if len(currBottom) == 1:
                return True

            if currBottom not in visited:
                visited[currBottom] = False
                for nextBottom in product(*(
                        memo[x + y]
                        for x, y in zip(currBottom, currBottom[1:])
                )):
                    if solve(nextBottom):
                        visited[currBottom] = True
                        break

            return visited[currBottom]

        memo = defaultdict(list)
        for s in allowed:
            memo[s[:2]].append(s[2])

        visited = {}
        return solve(bottom)


print(Solution().pyramidTransition(
    'AABA', ["AAA", "AAB", "ABA", "ABB", "BAC"]))
