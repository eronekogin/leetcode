"""
https://leetcode.com/problems/rearrange-spaces-between-words/
"""


class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        spaceLen = len(text) - sum(len(w) for w in words)
        if len(words) == 1:
            return words[0] + ' ' * spaceLen

        sepSpace, remainSpace = divmod(spaceLen, len(words) - 1)
        newWords: list[str] = []
        for w in words:
            newWords.append(w)
            newWords.append(' ' * sepSpace)

        newWords.pop()
        newWords.append(' ' * remainSpace)
        return ''.join(newWords)
