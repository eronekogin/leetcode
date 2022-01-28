"""
https://leetcode.com/problems/maximum-score-words-formed-by-letters/
"""

from collections import Counter


class Solution:
    def maxScoreWords(
        self,
        words: list[str],
        letters: list[str],
        score: list[int]
    ) -> int:
        def dfs(start: int, currScore: int, remainCnt: Counter) -> None:
            self.maxScore = max(self.maxScore, currScore)
            for end, wordCnt in enumerate(wordCnts[start:], start):
                # Check if there is still enough letters to construct the
                # current word.
                if not wordCnt - remainCnt:
                    dfs(end + 1, currScore +
                        wordScores[end], remainCnt - wordCnt)

        OFFSET = ord('a')
        wordScores = [sum(score[ord(c) - OFFSET] for c in w) for w in words]
        wordCnts = [Counter(w) for w in words]

        self.maxScore = 0
        dfs(0, 0, Counter(letters))
        return self.maxScore
