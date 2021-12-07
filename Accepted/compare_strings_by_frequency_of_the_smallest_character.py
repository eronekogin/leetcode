"""
https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/
"""


from collections import Counter
from bisect import bisect_right


class Solution:
    def numSmallerByFrequency(
        self, queries: list[str], words: list[str]
    ) -> list[int]:
        def f(w: str) -> int:
            cnt = Counter(w)
            return cnt[sorted(cnt.keys())[0]]

        freqs = sorted(map(f, words))
        N = len(freqs)
        return list(map(lambda q: N - bisect_right(freqs, f(q)), queries))


print(Solution().numSmallerByFrequency(
    ["bbb", "cc"],
    ["a", "aa", "aaa", "aaaa"]))
