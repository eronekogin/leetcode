"""
https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_partition(self, s: str, k: int) -> int:
        """
        minimum partition
        """
        parts = 0
        curr = 0
        for x in map(int, s):
            curr = curr * 10 + x
            if k >= curr:
                continue

            if x > k:
                return -1

            curr = x
            parts += 1

        return parts + 1


print(Solution().minimum_partition('165462', 60))
