"""
https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
"""


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        def dfs(remainDices: int, remainSum: int) -> int:
            if remainDices == 0:  # Used all dices.
                if remainSum == 0:  # Found a solution.
                    return 1
                else:  # Not enough sum from all dices.
                    return 0

            if (remainDices, remainSum) not in memo:
                cnt = 0
                for newRemainSum in range(max(0, remainSum - f), remainSum):
                    cnt += dfs(remainDices - 1, newRemainSum)

                memo[(remainDices, remainSum)] = cnt

            return memo[(remainDices, remainSum)]

        memo = {}
        return dfs(d, target) % (10 ** 9 + 7)
