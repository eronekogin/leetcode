"""
https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/description/
"""


class Solution:
    """
    Solution
    """

    def find_maximum_elegance(self, items: list[list[int]], k: int) -> int:
        """
        sort the items by profit in descending order, then the first k
        items are the biggest total profits we could get.

        Then iterate through the remaining n - k items and replace the smallest
        duplicate profit for an exiting category if the current item's category
        is not visited before.

        Keep doing so until no more duplicate profit found for each item and 
        we have found our maximum elegance.
        """
        items.sort(key=lambda x: -x[0])
        max_elegance = curr_profit = 0
        duplicated_profits: list[int] = []
        visited_categories: set[int] = set()

        for i, (p, c) in enumerate(items):
            if i < k:
                if c in visited_categories:
                    duplicated_profits.append(p)

                curr_profit += p
            elif c not in visited_categories:
                if not duplicated_profits:
                    break

                curr_profit += p - duplicated_profits.pop()

            visited_categories.add(c)
            max_elegance = max(
                max_elegance,
                curr_profit + len(visited_categories) ** 2
            )

        return max_elegance
