"""
https://leetcode.com/problems/largest-palindromic-number/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def largest_palindromic(self, num: str) -> str:
        """
        largest palindromic
        """
        cnt = Counter(num)
        mid = next((c for c in '9876543210' if cnt[c] & 1), '')
        half = ''.join(c * (cnt[c] >> 1) for c in '0123456789')
        return (half[::-1] + mid + half).strip('0') or '0'


print(Solution().largest_palindromic("00000"))
