"""
https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/description
"""


from itertools import accumulate


class Solution:
    """
    Solution
    """

    def max_total_fruits(self, fruits: list[list[int]], start_pos: int, k: int) -> int:
        """
        max_total_fruits
        """
        right_boundary = max(start_pos, fruits[-1][0])
        amount = [0] * (1 + right_boundary)
        for pos, amt in fruits:
            amount[pos] = amt

        prefix_sums = [0] + list(accumulate(amount))
        max_collected_fruits = 0

        # Go right first then turn left.
        for right_distance in range(min(k, right_boundary - start_pos) + 1):
            left_distance = max(0, k - 2 * right_distance)

            l = max(0, start_pos - left_distance)
            r = start_pos + right_distance

            max_collected_fruits = max(
                max_collected_fruits,
                prefix_sums[r + 1] - prefix_sums[l]
            )

        # Go left first then turn right.
        for left_distance in range(min(k, start_pos) + 1):
            right_distance = max(0, k - 2 * left_distance)

            l = start_pos - left_distance
            r = min(right_boundary, start_pos + right_distance)

            max_collected_fruits = max(
                max_collected_fruits,
                prefix_sums[r + 1] - prefix_sums[l]
            )

        return max_collected_fruits
