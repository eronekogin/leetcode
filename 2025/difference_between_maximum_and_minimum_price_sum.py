"""
https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/description/
"""


from collections import defaultdict


class Solution:
    """
    Solution
    """

    def max_output(self, n: int, edges: list[list[int]], price: list[int]) -> int:
        """
        max output
        """
        def get_max_sum(curr: int, parent: int) -> int:
            max_child_sum = 0
            for child in graph[curr]:
                if child == parent:
                    continue

                max_child_sum = max(max_child_sum, get_max_sum(child, curr))

            subtree_sums[curr] = max_child_sum + price[curr]
            return subtree_sums[curr]

        def get_top_2_subtrees(curr: int, parent: int):
            i1 = i2 = -1
            s1 = s2 = 0
            for child in graph[curr]:
                if child == parent:
                    continue

                if subtree_sums[child] > s2:
                    i2, s2 = child, subtree_sums[child]

                if s2 > s1:
                    s1, s2 = s2, s1
                    i1, i2 = i2, i1

            return (i1, s1, i2, s2)

        def reroot(curr: int, parent: int, parent_contribution: int):
            i1, s1, _, s2 = get_top_2_subtrees(curr, parent)
            nonlocal max_cost

            # The path can go to its top 1 sub tree or go to its parent
            max_cost = max(
                max_cost,
                parent_contribution,
                s1
            )

            for child in graph[curr]:
                if child == parent:
                    continue

                if child == i1:
                    reroot(
                        child,
                        curr,
                        price[curr] + max(s2, parent_contribution)
                    )
                else:
                    reroot(
                        child,
                        curr,
                        price[curr] + max(s1, parent_contribution)
                    )

        subtree_sums: list[int] = [0] * n
        graph: defaultdict[int, list[int]] = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        max_cost = -1
        get_max_sum(0, -1)
        reroot(0, -1, 0)
        return max_cost
