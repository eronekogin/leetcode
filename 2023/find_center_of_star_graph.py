"""
https://leetcode.com/problems/find-center-of-star-graph/
"""


class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        n = len(edges) + 1
        cnt = [0] * n
        for u, v in edges:
            cnt[u - 1] += 1
            cnt[v - 1] += 1

            if cnt[u - 1] == n - 1:
                return u

            if cnt[v - 1] == n - 1:
                return v

        return -1  # Not found.
