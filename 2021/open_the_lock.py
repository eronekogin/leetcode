"""
https://leetcode.com/problems/open-the-lock/
"""


from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        currNodes, stepCnt = ['0000'], -1
        visited = set(deadends)
        while currNodes:
            stepCnt += 1
            nextNodes = []
            for node in currNodes:
                if node == target:
                    return stepCnt
                elif node not in visited:
                    visited.add(node)
                    for i, c in enumerate(node):
                        nextNodes.append(
                            node[:i] + str((int(c) - 1) % 10) + node[i + 1:])
                        nextNodes.append(
                            node[:i] + str((int(c) + 1) % 10) + node[i + 1:])

            currNodes = nextNodes

        return -1  # The target is not reachable.


print(Solution().openLock(["0201", "0101", "0102", "1212", "2002"], "0202"))
