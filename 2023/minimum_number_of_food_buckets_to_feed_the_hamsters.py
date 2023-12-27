"""
https://leetcode.com/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/
"""


class Solution:
    """
    Solution
    """

    def minimum_buckets(self, hamsters: str) -> int:
        """
        minimum_buckets
        """
        if (
            'HHH' in hamsters or
            hamsters.startswith('HH.') or
            hamsters.endswith('.HH') or
            '.' not in hamsters
        ):
            return -1

        total_hamster = hamsters.count('H')
        dup_bucket = hamsters.count('H.H')

        return total_hamster - dup_bucket
