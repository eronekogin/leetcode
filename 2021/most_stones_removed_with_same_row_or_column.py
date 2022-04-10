"""
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
"""


class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        """
        1. All the connected stones could be removed until one stone. Then the
            total stones - the remaining stones will be the total removed
            stones.
        2. One stone is connected to another if they share the same row or col,
            in other words, a stone connects a row index and a col index.
        3. So instead of couting connected stones, we count connected indexes,
            here in order to make all the index unique, we could use ~col to
            different it with row index.
        4. Then we could use union find to union all the connected stones,
            and later the total number of disjoint sets is the total number of
            remaining stone.
        """
        def find(x: int) -> int:
            if x != uf[x]:
                uf[x] = find(uf[x])

            return uf[x]

        def union(x: int, y: int) -> None:
            uf.setdefault(x, x)
            uf.setdefault(y, y)
            uf[find(x)] = find(y)

        uf = {}

        for r, c in stones:
            union(r, ~c)

        return len(stones) - len({find(x) for x in uf})


print(Solution().removeStones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]))
