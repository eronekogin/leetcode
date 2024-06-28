"""
https://leetcode.com/problems/rearrange-characters-to-make-target-string/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def rearrange_characters(self, s: str, target: str) -> int:
        """
        rearrange characters
        """
        cnt = Counter(s)
        cnt2 = Counter(target)
        return min(cnt[c] // f for c, f in cnt2.items())
