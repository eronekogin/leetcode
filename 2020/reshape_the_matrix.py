"""
https://leetcode.com/problems/reshape-the-matrix/
"""


from typing import List, Iterator


class Solution:
    def matrixReshape(
            self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        def old_matrix() -> Iterator[int]:
            for row in nums:
                for num in row:
                    yield num

        if r * c != len(nums) * len(nums[0]):  # No possible solution.
            return nums

        newMatrix = [[None] * c for _ in range(r)]
        nr = nc = 0
        for num in old_matrix():
            if nc == c:
                nc = 0
                nr += 1

            newMatrix[nr][nc] = num
            nc += 1

        return newMatrix
