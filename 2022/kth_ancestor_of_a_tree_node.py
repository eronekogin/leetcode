"""
https://leetcode.com/problems/kth-ancestor-of-a-tree-node/
"""


class TreeAncestor:
    """
    1. Initial parent stands for 1 step parent for each node.
    2. Then we can have 2 steps parent for each node, 4 steps parent for each
        node until we reach 1 << maxStep steps parent for each node.
    """

    def __init__(self, n: int, parent: list[int]):
        self.maxStep = 15
        currMemo = dict(enumerate(parent))  # One step jump.
        jumps = [currMemo]

        for _ in range(self.maxStep):
            nextMemo = {}

            for node in currMemo:
                if currMemo[node] in currMemo:
                    nextMemo[node] = currMemo[currMemo[node]]

            jumps.append(nextMemo)
            currMemo = nextMemo

        self.jumps = jumps

    def getKthAncestor(self, node: int, k: int) -> int:
        jumpStep = self.maxStep
        parent = node
        cnt = k
        while cnt > 0 and parent > -1:
            if cnt >= (1 << jumpStep):
                parent = self.jumps[jumpStep].get(parent, -1)
                cnt -= (1 << jumpStep)
            else:
                jumpStep -= 1

        return parent


t = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
print(t.getKthAncestor(3, 1))
