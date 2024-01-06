"""
https://leetcode.com/problems/valid-arrangement-of-pairs/
"""


from collections import defaultdict, Counter


class Solution:
    """
    Solution
    """

    def valid_arrangement(self, pairs: list[list[int]]) -> list[list[int]]:
        """
        valid_arrangement
        """
        g = defaultdict(list)  # graph
        din, dout = Counter(), Counter()  # in degree, out degree
        for u, v in pairs:
            g[u].append(v)
            dout[u] += 1
            din[v] += 1

        s = pairs[0][0]  # Start anywhere if it's an Eulerian cycle.
        for p in dout:
            if dout[p] - din[p] == 1:  # It's an Eulerian trail. Have to start here
                s = p
                break

        # Hierholzer's Algorithm:
        route = []
        st = [s]
        while st:
            while g[st[-1]]:
                st.append(g[st[-1]].pop())
            route.append(st.pop())
        route.reverse()
        return [[route[i], route[i+1]] for i in range(len(route)-1)]
