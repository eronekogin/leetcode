"""
https://leetcode.com/problems/search-suggestions-system/
"""


from bisect import bisect_left


class Solution:
    def suggestedProducts(
        self,
        products: list[str],
        searchWord: str
    ) -> list[list[str]]:
        sortedWords = sorted(products)
        prefix = ''
        rslt = []
        start = 0
        for c in searchWord:
            prefix += c
            start = bisect_left(sortedWords, prefix, start)
            rslt.append([
                w
                for w in sortedWords[start: start + 3]
                if w.startswith(prefix)
            ])

        return rslt
