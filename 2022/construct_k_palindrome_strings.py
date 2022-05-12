"""
https://leetcode.com/problems/construct-k-palindrome-strings/
"""


from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        """
        The question is actually asking if we can construct exact k
        palindrome by using up all chars in s:

        Restriction #1:
            The number of odd chars (chars occurring odd times in s) should be
            less than k, otherwise we have more than k palindrome to form
            after using all chars in s, as we must deal with those odd chars
            by putting them in the middle to form a new palindrome.

        Restriction #2:
            k must be less than the length of s as at least one char must
            exist in each palindrome.
        """
        cnt = Counter(s)
        oddChars = sum(v & 1 for v in cnt.values())
        return oddChars <= k <= len(s)
