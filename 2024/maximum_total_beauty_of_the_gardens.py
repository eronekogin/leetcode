"""
https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/description/
"""


from bisect import bisect_right, bisect_left


class Solution:
    """
    Solution
    """

    def maximum_beauty(
        self,
        flowers: list[int],
        new_flowers: int,
        target: int,
        full: int,
        partial: int
    ) -> int:
        """
        maximum beauty
        """
        n = len(flowers)
        sorted_flowers = sorted(min(target, f) for f in flowers)

        if sorted_flowers[0] == target:  # All gardens are full.
            return full * n

        # Enough flowers to make all gardens full.
        if new_flowers >= target * n - sum(sorted_flowers):
            return max(full * n, full * (n - 1) + partial * (target - 1))

        # Build the cost array, cost[i] indicates how many new flowers
        # needed to make 0 to i - 1 gardens to have flowers same as
        # sorted_flowers[i].
        costs: list[int] = [0]
        for i in range(1, n):
            costs.append(
                costs[-1] +
                i * (sorted_flowers[i] - sorted_flowers[i - 1])
            )

        # Find the first garden that is already completed.
        end = bisect_left(sorted_flowers, target) - 1

        max_score = 0
        remain_flowers = new_flowers
        while remain_flowers >= 0:
            i = min(end, bisect_right(costs, remain_flowers) - 1)

            partial_garden = (
                sorted_flowers[i] +
                (remain_flowers - costs[i]) // (i + 1)
            )
            max_score = max(
                max_score,
                full * (n - end - 1) + partial * partial_garden
            )

            # Complete the end garden
            remain_flowers -= target - sorted_flowers[end]
            end -= 1

        return max_score
