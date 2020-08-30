"""
https://leetcode.com/problems/pancake-sorting/
"""


from typing import List


class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        def flip(end: int) -> None:
            l, r = 0, end
            while l < r:
                A[l], A[r] = A[r], A[l]
                idxMemo[A[l]], idxMemo[A[r]] = l, r
                l += 1
                r -= 1

        flipPositions, idxMemo = [], {v: i for i, v in enumerate(A)}

        # No need to check the last element as it should be in its right
        # position when the remaining numbers are sorted.
        for currMax in range(len(A), 1, -1):
            currPos = idxMemo[currMax]
            if currPos != currMax - 1:
                # If the current max number is not in its supposed position
                # or not already at the start of the list, flip the current
                # max number to the start of the list first.
                if currPos > 0:
                    flipPositions.append(currPos + 1)
                    flip(currPos)

                # Then flip the current max number to where it should be.
                flipPositions.append(currMax)
                flip(currMax - 1)

        return flipPositions


print(Solution().pancakeSort([3, 2, 4, 1]))
