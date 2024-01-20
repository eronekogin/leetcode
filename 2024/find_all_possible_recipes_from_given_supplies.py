"""
https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/
"""


from functools import cache
from collections import defaultdict


class Solution:
    """
    Solution
    """

    def find_all_recipes(
        self,
        recipes: list[str],
        ingredients: list[list[str]],
        supplies: list[str]
    ) -> list[str]:
        """
        find_all_recipes
        """
        @cache
        def dfs(node: str):
            if node in visited:  # Cycle
                return False

            visited.add(node)

            if node not in graph:
                return False

            for next_node in graph[node]:
                if next_node not in supply_set and not dfs(next_node):
                    return False

            return True

        supply_set = set(supplies)

        graph: defaultdict[str, list[str]] = defaultdict(list)
        for r, items in zip(recipes, ingredients):
            graph[r].extend(items)

        visited = set()
        rslt = []

        for r in recipes:
            if dfs(r):
                rslt.append(r)

        return rslt
