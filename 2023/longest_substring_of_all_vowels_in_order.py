"""
https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/
"""


class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        seen = set()
        maxLen = 0
        start = -1
        for end, c in enumerate(word):
            if end > 0 and c < word[end - 1]:
                seen = set()
                start = end - 1

            seen.add(c)
            if len(seen) == 5:
                maxLen = max(maxLen, end - start)

        return maxLen


print(Solution().longestBeautifulSubstring("aeiaaioaaaaeiiiiouuuooaauuaeiu"))
