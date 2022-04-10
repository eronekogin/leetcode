"""
https://leetcode.com/problems/cracking-the-safe/
"""


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        """
        1. Since the total combination of the passwords could be k^n, in order
            to find a sequence which contains all the combinations,
            we should make each combination occurs once in our sequence.

        2. Then if we take each combination of n-1 digits as a node, and each
            node has k edges to other nodes having the first digit of the 
            current node removed and append a new digit at the end.
            For example, if n = 2 and k = 2, then we have two nodes 0 and 1.
            Each node has 2 edges 0 and 1.

        3. Then our goal is to find a Euler circuit (a path which walks every
            edge in this graph only once and back to where it is started) in
            this graph and we could apply Hierholzer's algorithm.
        """
        def walk(currNode: str) -> None:
            for option in EDGES_OPTIONS:
                edge = currNode + option
                if edge not in visitedEdges:
                    visitedEdges.add(edge)
                    walk(edge[1:])  # Walk on other nodes first.
                    path.append(option)  # Then append the current option.

        EDGES_OPTIONS = [str(i) for i in range(k)]
        visitedEdges = set()
        path = []
        start = '0' * (n - 1)
        walk(start)
        return ''.join(path) + start


print(Solution().crackSafe(2, 2))
