"""
https://leetcode.com/problems/print-words-vertically/
"""


from itertools import zip_longest


class Solution:
    def printVertically(self, s: str) -> list[str]:
        return [
            ''.join(chars).rstrip()
            for chars in zip_longest(*(s.split()), fillvalue=' ')
        ]


print(Solution().printVertically("TO BE OR NOT TO BE"))
