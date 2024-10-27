"""
https://leetcode.com/problems/number-of-good-paths/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def number_of_good_paths(self, vals: list[int], edges: list[list[int]]) -> int:
        """
        number of good paths
        """
        def find(x: int) -> int:
            if f[x] != x:
                f[x] = find(f[x])

            return f[x]

        rslt = n = len(vals)
        f = list(range(n))
        cnt = [Counter({x: 1}) for x in vals]

        for v, i, j in sorted((max(vals[i], vals[j]), i, j) for i, j in edges):
            fi, fj = find(i), find(j)
            ci, cj = cnt[fi][v], cnt[fj][v]

            rslt += ci * cj

            f[fj] = fi
            cnt[fi] = Counter({v: ci + cj})

        return rslt
