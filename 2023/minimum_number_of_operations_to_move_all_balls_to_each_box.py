"""
https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
"""


class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        posOfOnes = [i for i, c in enumerate(boxes) if c == '1']
        return [
            sum(
                abs(i - j)
                for j in posOfOnes
            )
            for i in range(len(boxes))
        ]
