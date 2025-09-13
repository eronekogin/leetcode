"""
https://leetcode.com/problems/relocate-marbles/description/
"""


class Solution:
    """
    Solution
    """

    def relocate_marbles(
        self,
        nums: list[int],
        move_from: list[int],
        move_to: list[int]
    ) -> list[int]:
        """
        relocate marbles
        """
        positions = set(nums)
        for f, t in zip(move_from, move_to):
            if f == t:
                continue

            positions.add(t)
            positions.remove(f)

        return sorted(positions)


print(Solution().relocate_marbles(
    [3, 4], [4, 3, 1, 2, 2, 3, 2, 4, 1], [3, 1, 2, 2, 3, 2, 4, 1, 1]))
