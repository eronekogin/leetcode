"""
https://leetcode.com/problems/two-city-scheduling/
"""


from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        rslt = 0
        for ca, cb in costs:
            rslt += ca
            diff.append(cb - ca)

        return rslt + sum(sorted(diff)[:(len(costs) >> 1)])
