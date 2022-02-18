"""
https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/
"""

from collections import Counter


class Solution:
    def maxFreq(
        self,
        s: str,
        maxLetters: int,
        minSize: int,
        maxSize: int
    ) -> int:
        """
        1. If a string has x occurrences, its substring must occur at least x
            times.
        2. A substring must have minSize length.
        3. So we could simply count all substring with minSize length, then
            check if each substring satisfy the conditions.
        4. Notice that maxSize is not needed in this case as we are counting
            the maximum number of occurrences for a substring, and if the
            substring is longer than the minSize, it must have less occurrences.
        """
        cnt = Counter(s[i:i + minSize] for i in range(len(s) - minSize + 1))
        return max([cnt[w] for w in cnt if len(set(w)) <= maxLetters] or [0])
