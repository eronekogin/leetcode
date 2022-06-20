"""
https://leetcode.com/problems/rearrange-words-in-a-sentence/
"""


class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split()
        words[0] = words[0].lower()

        # Python's sorted function is guarenteed to be stable, which means
        # it will keep the original order of the items if two item's
        # comparision result is the same.
        sortedWords = sorted(words, key=len)
        sortedWords[0] = sortedWords[0].title()
        return ' '.join(sortedWords)
