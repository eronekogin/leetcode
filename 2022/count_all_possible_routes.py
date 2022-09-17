"""
https://leetcode.com/problems/count-all-possible-routes/
"""


from functools import lru_cache


class Solution:
    def countRoutes(
        self,
        locations: list[int],
        start: int,
        finish: int,
        fuel: int
    ) -> int:
        @lru_cache(None)
        def dfs(currCity: int, remainFuel: int) -> int:
            if remainFuel < 0:
                return 0

            cnt = 0
            if currCity == finish:
                cnt += 1

            for nextCity in range(len(locations)):
                if nextCity != currCity:
                    cnt += dfs(
                        nextCity,
                        remainFuel -
                        abs(locations[nextCity] - locations[currCity])
                    )

            return cnt

        return dfs(start, fuel) % (10 ** 9 + 7)
