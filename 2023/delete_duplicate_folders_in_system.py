"""
https://leetcode.com/problems/delete-duplicate-folders-in-system/
"""


from collections import defaultdict


class Node:
    def __init__(self) -> None:
        self.child = defaultdict(Node)
        self.isDeleted = False


class Solution:
    def deleteDuplicateFolder(self, paths: list[list[str]]) -> list[list[str]]:
        def dfs1(node: Node):
            key = '(' + ''.join(c + dfs1(node.child[c]) for c in node.child) + ')'
            if key != '()':  # Not empty sub tree.
                pattern[key].append(node)
            
            return key

        def dfs2(node: Node, path: list[str]):
            for c in node.child:
                if not node.child[c].isDeleted:
                    dfs2(node.child[c], path + [c])
            
            if path:
                rslt.append(path[:])

        pattern: defaultdict[str, list[Node]] = defaultdict(list)
        root = Node()
        rslt: list[list[str]] = []

        # Create Trie first.
        for path in sorted(paths):
            node = root
            for c in path:
                node = node.child[c]
        
        dfs1(root)

        # Mark duplicated sub folder pattern as deleted.
        for nodes in pattern.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.isDeleted = True

        dfs2(root, [])
        return rslt

