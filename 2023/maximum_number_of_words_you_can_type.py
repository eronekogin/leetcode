"""
https://leetcode.com/problems/maximum-number-of-words-you-can-type/
"""


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        target = set(brokenLetters)
        cnt = 0
        for w in text.split():
            wordSet = set(w)
            if any(c in wordSet for c in target):
                continue

            cnt += 1
        
        return cnt