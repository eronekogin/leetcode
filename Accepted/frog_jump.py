"""
https://leetcode.com/problems/frog-jump/
"""


from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        allStones, faliPath = set(stones), set()
        stack = [(0, 0)]  # (current stone, pre jump step)
        lastStone = stones[-1]
        while stack:
            currStone, preStep = stack.pop()
            for currStep in (preStep - 1, preStep, preStep + 1):
                nextStone = currStone + currStep
                if currStep > 0 and nextStone in allStones and (
                        nextStone, currStep) not in faliPath:
                    if nextStone == lastStone:
                        return True

                    stack.append((nextStone, currStep))

            faliPath.add((currStone, preStep))

        return False


print(Solution().canCross([0, 1, 2, 3, 4, 8, 9, 11]))
