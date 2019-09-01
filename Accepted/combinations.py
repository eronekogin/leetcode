"""
https://leetcode.com/problems/combinations/
"""

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Use backtracking solution.
        """
        rslt, workStack = [], []
        nextNum, maxStart = 1, n + 1 - k
        while True:
            if len(workStack) == k:  # Found a combination.
                rslt.append(workStack.copy())
                nextNum = workStack.pop() + 1

            if nextNum > maxStart + len(workStack):
                # maxStart means the start position for the maximum start
                # number in n so that range [start, n] has a length k.
                # So the workList[i]'s maximum number should be start + k.
                # And if it is bigger than that number, it means in the end
                # it will not have enough numbers in range [0, n] to be added
                # to the target sequence.
                if not workStack:  # Stack is empty, no more combinations.
                    return rslt

                nextNum = workStack.pop() + 1
            else:
                workStack.append(nextNum)
                nextNum += 1

    def combine2(self, n: int, k: int) -> List[List[int]]:
        """
        Using sliding index, which is an interesting solution.
        And it is actually just another implementation of backtracing
        without using stack.
        """
        rslt, workList = [], [0] * k
        i, maxStart = 0, n + 1 - k
        while i >= 0:
            workList[i] += 1
            if workList[i] > maxStart + i:
                # maxStart means the start position for the maximum start
                # number in n so that range [start, n] has a length k.
                # So the workList[i]'s maximum number should be start + k.
                # And if it is bigger than that number, it means in the end
                # it will not have enough numbers in range [0, n] to be added
                # to the target sequence.
                # So we move index to the left.
                i -= 1
            elif i == k - 1:  # Found a combination.
                rslt.append(workList.copy())
            else:  # Move index to the right and copy previous value.
                i += 1
                workList[i] = workList[i - 1]

        return rslt


print(Solution().combine2(4, 3))
