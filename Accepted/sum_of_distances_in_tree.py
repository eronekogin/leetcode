"""
https://leetcode.com/problems/sum-of-distances-in-tree/
"""


from collections import defaultdict


class Solution:
    def sumOfDistancesInTree(
            self, N: int, edges: list[list[int]]) -> list[int]:
        """
        1. Suppose count[x] stands for the number of nodes in the subtree
            rooted by node x, and sumdis[x] stands for the sum of distances
            between node x and all the nodes in the subtree, then we have:

            For child in subtree:
                count[x] = sum(count[child])
                sumdis[x] = sum(sumdis[child] + count[child])

        2. Suppose an edge connects to node x and y, if we cut the edge to
            convert the original tree into two subtrees, then we have:
                ans[x] = sumdis[x] + sumdis[y] + count[y]
                ans[y] = sumdis[y] + sumdis[x] + count[x]

            Here ans[x] means the sum of distances from x to each any other
            nodes in the original tree.

        3. So ans[x] = ans[y] + count[y] - count[x]
            = ans[y] + N - 2 * count[x], here N is the total number of nodes
            in the original tree.
        """
        def count_nodes(currNode: int, parent: int) -> None:
            """
            1. Doing a post-order traverse to first traverse each child node,
                then traverse the root node.
            2. Count total nodes in the subtrees.
            3. Calculate the sum of distance for each root of the subtrees.
            """
            for child in graph[currNode]:
                if child != parent:  # Check nodes in the subtree.
                    count_nodes(child, currNode)
                    count[currNode] += count[child]
                    ans[currNode] += ans[child] + count[child]

        def calc_answer(currNode: int, parent: int) -> None:
            """
            1. Doing a pre-order traverse to first traverse the root, then
                traverse each child.
            2. Calculate the answer for each child based on
                ans[child] = ans[parent] + N - 2 * count[child]
            """
            for child in graph[currNode]:
                if child != parent:  # Check nodes in the subtree.
                    ans[child] = ans[currNode] + N - (count[child] << 1)
                    calc_answer(child, currNode)

        graph = defaultdict(set)
        for s, t in edges:
            graph[s].add(t)
            graph[t].add(s)

        ans = [0] * N
        count = [1] * N
        count_nodes(0, None)
        calc_answer(0, None)
        return ans
