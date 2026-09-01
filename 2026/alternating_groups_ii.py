"""
https://leetcode.com/problems/alternating-groups-ii/description/
"""


class Solution:
    """
    Solution
    """

    def number_of_alternating_groups(self, colors: list[int], k: int) -> int:
        """
        number of alternating groups
        """
        colors += colors[: k - 1]
        cnt = 0
        start = 0
        for end in range(1, len(colors)):
            if colors[end] != colors[end - 1]:
                if end - start + 1 == k:
                    cnt += 1
                    start += 1

                continue

            cnt += (end - start) == k
            start = end

        return cnt


print(Solution().number_of_alternating_groups([0, 1, 0, 0, 1, 0, 1], 6))
