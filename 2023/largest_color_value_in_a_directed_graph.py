"""
https://leetcode.com/problems/largest-color-value-in-a-directed-graph/
"""


class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        OFFSET = ord('a')
        N = len(colors)
        incoming = [0] * N
        graph = [[] for _ in range(N)]
        for u, v in edges:
            incoming[v] += 1
            graph[u].append(v)

        stack = [i for i in range(N) if incoming[i] == 0]
        freqs = [[0] * 26 for _ in range(N)]

        while stack:
            u = stack.pop()
            freqs[u][ord(colors[u]) - OFFSET] += 1

            for v in graph[u]:
                freqs[v] = list(map(max, freqs[v], freqs[u]))
                incoming[v] -= 1
                if incoming[v] == 0:
                    stack.append(v)

        if sum(incoming) > 0:  # Found cycle.
            return -1

        return max(max(nodeFreqs) for nodeFreqs in freqs)
