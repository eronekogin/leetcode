"""
https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/
"""


class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        cnt = [0] * 26
        OFFSET, N = ord('a'), len(words)

        for w in words:
            for c in w:
                cnt[ord(c) - OFFSET] += 1
        
        return all(x % N == 0 for x in cnt)