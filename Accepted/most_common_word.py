"""
https://leetcode.com/problems/most-common-word/
"""


from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        bannedWords = set(banned)
        words = ''.join(c.lower() if c.isalpha() else ' ' for c in paragraph)
        words = [w for w in words.split() if w not in bannedWords]
        cnt = Counter(words)
        return sorted(cnt.keys(), key=lambda w: -cnt[w])[0]


print(Solution().mostCommonWord(
    "Bob. hIt, baLl",
    ["bob", "hit"]))
