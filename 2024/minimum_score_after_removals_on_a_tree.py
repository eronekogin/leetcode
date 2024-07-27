"""
https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/description/
"""


from collections import defaultdict, deque


class Solution:
    """
    Solution
    """

    def minimum_score(self, nums: list[int], edges: list[list[int]]) -> int:
        """
        minimum score
        """
        n, m = len(nums), len(edges)

        graph: defaultdict[int, list[int]] = defaultdict(list)
        children: defaultdict[int, set[int]] = defaultdict(set)
        xors = list(nums)  # Subtree values xors
        degrees = [0] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degrees[u] += 1
            degrees[v] += 1

        all_xor = 0
        visited: set[int] = set()
        queue: deque[int] = deque()
        for i, x in enumerate(nums):
            all_xor ^= x
            if degrees[i] == 1:  # leaf node
                queue.append(i)
                visited.add(i)

        # Calculate xor for each sub tree
        while queue:
            curr = queue.popleft()
            for node in graph[curr]:
                if node not in visited:
                    children[node].add(curr)
                    children[node] |= children[curr]
                    xors[node] ^= xors[curr]

                degrees[node] -= 1
                if degrees[node] == 1:
                    visited.add(node)
                    queue.append(node)

        # Calculate for each pair
        rslt = 10 ** 12
        for i in range(m - 1):
            for j in range(i + 1, m):
                a, b = edges[i]
                if b in children[a]:
                    a, b = b, a

                c, d = edges[j]
                if d in children[c]:
                    c, d = d, c

                # 3 cases:
                #   c is a's child
                #   a is c's child
                #   a and b are two independent subtrees.
                if c in children[a]:
                    scores = [xors[c], xors[a] ^ xors[c], all_xor ^ xors[a]]
                elif a in children[c]:
                    scores = [xors[a], xors[c] ^ xors[a], all_xor ^ xors[c]]
                else:
                    scores = [xors[a], xors[c], all_xor ^ xors[a] ^ xors[c]]

                rslt = min(rslt, max(scores) - min(scores))

        return rslt
