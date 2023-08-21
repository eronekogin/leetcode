"""
https://leetcode.com/problems/maximum-genetic-difference-query/
"""


class TrieNode:
    def __init__(self):
        self.child = {}
        self.go = 0  # Number of elements goes through this node
    
    def increase(self, number: int, d: int):
        curr = self
        for i in range(17, -1, -1):
            bit = (number >> i) & 1
            if bit not in curr.child:
                curr.child[bit] = TrieNode()
            
            curr = curr.child[bit]
            curr.go += d
    
    def find_max(self, number: int):
        curr, rslt = self, 0
        for i in range(17, -1, -1):
            bit = (number >> i) & 1
            if (1 - bit) in curr.child and curr.child[1 - bit].go > 0:
                curr = curr.child[1 - bit]
                rslt |= (1 << i)
            else:
                curr = curr.child[bit]
        
        return rslt


class Solution:
    def maxGeneticDifference(self, parents: list[int], queries: list[list[int]]) -> list[int]:
        n, m, root = len(parents), len(queries), -1
        ans, trieNode = [-1] * m, TrieNode()
        graph, queryByNode = [[] for _ in range(n)], [[] for _ in range(n)]
        for i, p in enumerate(parents):
            if p == -1: root = i
            else: graph[p].append(i)

        for i, q in enumerate(queries):
            queryByNode[q[0]].append((q[1], i))  # node -> list of pairs (val, idx)

        def dfs(u):
            trieNode.increase(u, 1)
            for val, idx in queryByNode[u]:
                ans[idx] = trieNode.find_max(val)
            for v in graph[u]:
                dfs(v)
            trieNode.increase(u, -1)

        dfs(root)
        return ans
            
