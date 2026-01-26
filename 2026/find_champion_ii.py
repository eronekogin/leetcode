"""
https://leetcode.com/problems/find-champion-ii/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def find_champion(self, n: int, edges: list[list[int]]) -> int:
        """
        Docstring for find_champion

        :param self: Description
        :param n: Description
        :type n: int
        :param edges: Description
        :type edges: list[list[int]]
        :return: Description
        :rtype: int
        """
        in_degrees = [0] * n
        for _, v in edges:
            in_degrees[v] += 1

        candidate = -1
        candidate_count = 0
        for node in range(n):
            if in_degrees[node] == 0:
                candidate = node
                candidate_count += 1

        if candidate_count > 1:
            return -1

        return candidate


print(Solution().find_champion(3, [[0, 1], [1, 2], [0, 2]]))
