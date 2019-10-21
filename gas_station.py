"""
https://leetcode.com/problems/gas-station/
"""


from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gasRemain = gasRequired = start = 0
        for i in range(len(gas)):
            gasRemain += gas[i] - cost[i]
            if gasRemain < 0:  # Run out of gas from the last start station.
                gasRequired -= gasRemain
                start = i + 1  # Start at the new station.
                gasRemain = 0

        if gasRemain >= gasRequired:
            return start

        return -1  # No solution.


gas = [4, 5, 2, 6, 5, 3]
cost = [3, 2, 7, 3, 2, 9]
print(Solution().canCompleteCircuit(gas, cost))
