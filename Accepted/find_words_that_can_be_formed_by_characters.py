"""
https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
"""


from collections import Counter


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        def is_good_string(w: str) -> bool:
            return not (Counter(w) - cnt)

        cnt = Counter(chars)
        rslt = 0
        for w in words:
            if is_good_string(w):
                rslt += len(w)

        return rslt
