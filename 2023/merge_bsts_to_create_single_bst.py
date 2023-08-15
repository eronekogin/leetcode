"""
https://leetcode.com/problems/merge-bsts-to-create-single-bst/
"""


from test_helper import TreeNode
from collections import defaultdict


class Solution:
    def canMerge(self, trees: list[TreeNode]):
        def in_order(currVal: int):
            if currVal in seen:
                self.isInvalid = True
                return
            
            seen.add(currVal)
            node = nodes[currVal]
            if node.left:
                node.left = in_order(node.left.val)

            if currVal <= self.maxVal:
                self.isInvalid = True
                return
            
            self.maxVal = currVal

            if node.right:
                node.right = in_order(node.right.val)

            return node

        nodes = {}
        indegree = defaultdict(int)
        for tree in trees:
            if tree.val not in indegree:
                indegree[tree.val] = 0
            
            if tree.left:
                indegree[tree.left.val] += 1
                if tree.left.val not in nodes:
                    nodes[tree.left.val] = tree.left
            
            if tree.right:
                indegree[tree.right.val] += 1
                if tree.right.val not in nodes:
                    nodes[tree.right.val] = tree.right
            
            nodes[tree.val] = tree
        
        # If there is more than one tree with no leaf node, it is not possible to form a single BST.
        sources = [k for k, v in indegree.items() if v == 0]
        if len(sources) != 1:
            return None
        
        self.maxVal = float('-inf')
        self.isInvalid = False
        seen = set()

        root = in_order(sources[0])
        
        if len(seen) != len(nodes) or self.isInvalid:
            return None
        
        return root


