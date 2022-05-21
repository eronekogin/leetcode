"""
https://leetcode.com/problems/queries-on-a-permutation-with-key/
"""


class Solution:
    def processQueries(self, queries: list[int], m: int) -> list[int]:
        p = list(range(1, m + 1))
        rslt = [0] * len(queries)
        for i, q in enumerate(queries):
            rslt[i] = p.index(q)
            p.insert(0, p.pop(rslt[i]))

        return rslt


print(Solution().processQueries([3, 1, 2, 1], 5))
