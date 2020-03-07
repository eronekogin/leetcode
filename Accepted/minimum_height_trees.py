"""
https://leetcode.com/problems/minimum-height-trees/
"""


from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:  # Only has one node.
            return [0]

        adjs = [set() for _ in range(n)]
        for currNode, adjNode in edges:
            adjs[currNode].add(adjNode)
            adjs[adjNode].add(currNode)

        # Get leaves which are nodes having only 1 adjacent.
        currLeaves = [i for i in range(n) if len(adjs[i]) == 1]
        remainNodes = n
        while remainNodes > 2:
            remainNodes -= len(currLeaves)
            newLeaves = []
            for currNode in currLeaves:
                adjNode = adjs[currNode].pop()
                adjs[adjNode].remove(currNode)
                if len(adjs[adjNode]) == 1:  # Adjacent node becomes leaf now.
                    newLeaves.append(adjNode)

            currLeaves = newLeaves

        return currLeaves


print(Solution().findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))
