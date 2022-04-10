"""
https://leetcode.com/problems/prison-cells-after-n-days/
"""


from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        """
        1. The first and the last element will always become 0 after one
            transformation step.
        2. So the actual loop happened between the combinations of the 6
            numbers in the middle.
        3. If initially the first and the last number is not zero, after one
            transformation step, it will enter the loop.
        4. If initially the first and the last number are zeros, after one
            transformation step, it will still be inside that loop.
        5. So we tried to record all the previous unique states until an
            existing state is found again, where cycleLen will hold the total
            length of the cycle.
        6. Then the last state will be determined by the target index 
            as (N - 1) % cycleLen.
        """
        visited = []
        currState = self.get_next_state(cells)
        cycleLen = 0
        while currState not in visited:
            visited.append(currState)
            currState = self.get_next_state(currState)
            cycleLen += 1

        return visited[(N - 1) % cycleLen]

    def get_next_state(self, currState: List[int]) -> List[int]:
        nextState = [0] * 8
        for i in range(1, 7):
            nextState[i] = currState[i - 1] ^ currState[i + 1] ^ 1

        return nextState


print(Solution().prisonAfterNDays([1, 0, 0, 1, 0, 0, 1, 0], 1000000000))
