"""
https://leetcode.com/problems/guess-the-word/
"""


from collections import Counter


class Master:
    def guess(self, word: str) -> int:
        pass


class Solution:
    def findSecretWord(self, wordlist: List[str], master: Master) -> None:
        """
        1. For any two words, the 0 match rate is (25/26) ^ 6 = 79.03%, which
            means we have a greater chance to guess a zero match word from
            the wordlist against the secret word.
        2. Then in order to eliminate maximum unmatched words after one guess,
            we could try to pick up the word which has maximum number of 
            other words from the wordlist that has at least 1 match position to
            it.
        3. Since we have a greater chance to guess a zero match word, we could
            then elminate any words that has a match to it, which then could
            reduce the remaining wordlist faster.
        """
        def get_match_degree(w1: str, w2: str) -> int:
            return sum(c1 == c2 for c1, c2 in zip(w1, w2))

        WORD_LEN = 6
        match_degree = 0
        remaingWords = wordlist
        while match_degree < WORD_LEN:
            cnt = [
                Counter(w[i] for w in remaingWords) for i in range(WORD_LEN)]
            candidate = max(
                remaingWords,
                key=lambda w: sum(cnt[i][c] for i, c in enumerate(w)))
            match_degree = master.guess(candidate)
            remaingWords = [
                w for w in remaingWords
                if get_match_degree(w, candidate) == match_degree]
