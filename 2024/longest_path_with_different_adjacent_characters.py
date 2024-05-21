"""
https://leetcode.com/problems/longest-path-with-different-adjacent-characters/description/
"""


class Solution:
    """
    Solution
    """

    def longest_path(self, parent: list[int], s: str) -> int:
        """
        longest path
        """
        def dfs(node: int) -> int:
            """
            stands for the longest path starting at node i
            """
            nonlocal max_len
            m1 = m2 = 0
            for c in children[node]:
                curr = dfs(c)
                if s[node] != s[c]:
                    if curr > m1:
                        m1, m2 = curr, m1
                    elif curr > m2:
                        m2 = curr

            max_len = max(max_len, m1 + m2 + 1)
            return m1 + 1

        children = [[] for _ in range(len(s))]
        for c, p in enumerate(parent):
            if p >= 0:
                children[p].append(c)

        max_len = 1
        dfs(0)
        return max_len
