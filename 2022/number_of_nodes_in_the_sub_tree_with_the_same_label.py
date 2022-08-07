"""
https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/
"""


from collections import defaultdict, Counter


class Solution:
    def countSubTrees(
        self,
        n: int,
        edges: list[list[int]],
        labels: str
    ) -> list[int]:
        def build_tree(root: int, parent: int) -> Counter[str]:
            label = labels[root]
            totalCnt = Counter(label)
            for subNode in graph[root]:
                if subNode != parent:
                    totalCnt += build_tree(subNode, root)

            rslt[root] = totalCnt[label]
            return totalCnt

        # Build graph.
        graph = defaultdict(list)
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)

        rslt = [0] * n
        build_tree(0, -1)
        return rslt


print(Solution().countSubTrees(4,
                               [[0, 2], [0, 3], [1, 2]],
                               "aeed"))
