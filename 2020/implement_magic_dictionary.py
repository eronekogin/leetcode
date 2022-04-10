"""
https://leetcode.com/problems/implement-magic-dictionary/
"""


from typing import List
from collections import defaultdict


class MagicDictionary:

    def __init__(self):
        self.memo = defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for w in dictionary:
            self.memo[len(w)].append(w)

    def search(self, searchWord: str) -> bool:
        for w in self.memo[len(searchWord)]:
            if sum(c1 != c2 for c1, c2 in zip(w, searchWord)) == 1:
                return True

        return False
