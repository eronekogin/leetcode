"""
https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/
"""


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        """
        Work backwords from nums to initial array, the divide by 2 operation
        can only be called when all the numbers in nums are even.
        """
        currNodes = [num for num in nums if num > 0]
        steps = 0
        while currNodes:
            nextNodes: list[int] = []
            nonZeroCnt = len(currNodes)
            for i in range(len(currNodes)):
                if currNodes[i] & 1 > 0:
                    steps += 1
                    currNodes[i] -= 1
                    nonZeroCnt -= currNodes[i] == 0

            if nonZeroCnt > 0:
                steps += 1  # Divide all by 2.
                for node in currNodes:
                    if node > 0:
                        nextNodes.append(node >> 1)

            currNodes = nextNodes

        return steps


print(Solution().minOperations([1, 5]))
