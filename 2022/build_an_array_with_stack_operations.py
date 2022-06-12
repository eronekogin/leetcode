"""
https://leetcode.com/problems/build-an-array-with-stack-operations/
"""


class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        ops: list[str] = []
        iTarget = 0
        for num in range(1, n + 1):
            if num != target[iTarget]:
                ops.extend(['Push', 'Pop'])
            else:
                ops.append('Push')
                iTarget += 1

            if iTarget == len(target):
                break

        return ops
