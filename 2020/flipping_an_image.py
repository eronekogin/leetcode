"""
https://leetcode.com/problems/flipping-an-image/
"""


from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[item ^ 1 for item in reversed(row)] for row in A]


print(Solution().flipAndInvertImage(
    [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
))
