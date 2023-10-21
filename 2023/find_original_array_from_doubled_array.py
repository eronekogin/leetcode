"""
https://leetcode.com/problems/find-original-array-from-doubled-array/
"""


from collections import Counter


class Solution:
    """
    Solution.
    """

    def find_original_array(self, changed: list[int]) -> list[int]:
        """
        find_original_array
        """
        if len(changed) & 1:  # Odd length.
            return []

        cnt = Counter(changed)
        if cnt[0] & 1:  # Unmatched zero pairs.
            return []

        for x in sorted(cnt):
            if cnt[x] > cnt[x << 1]:  # Unmatched x pairs.
                return []

            cnt[x << 1] -= cnt[x] if x > 0 else cnt[x] >> 1

        return list(cnt.elements())
