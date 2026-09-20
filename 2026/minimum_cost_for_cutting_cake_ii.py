"""
https://leetcode.com/problems/minimum-cost-for-cutting-cake-ii/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_cost(self, m: int, n: int, h: list[int], v: list[int]) -> int:
        """
        minimum cost
        """
        h.sort()
        v.sort()
        cost = 0
        sh, sv = sum(h), sum(v)

        while h and v:
            if h[-1] > v[-1]:
                cost += h[-1] + sv
                sh -= h.pop()
            else:
                cost += v[-1] + sh
                sv -= v.pop()

        return cost + sh + sv
