"""
https://leetcode.com/problems/swap-for-longest-repeated-character-substring/
"""


from itertools import groupby
from collections import Counter


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        groups = [[c, len(list(g))] for c, g in groupby(text)]
        cnt = Counter(text)

        # Calculate initial max length for each group by only extending
        # one character in case there is more left in the remaining text.
        maxCnt = max(min(l + 1, cnt[c]) for c, l in groups)

        # Then try to merge two groups together if they are only separated by
        # a single different char but having the same chars before and after.
        for i in range(1, len(groups) - 1):
            if groups[i - 1][0] == groups[i + 1][0] and groups[i][1] == 1:
                maxCnt = max(
                    maxCnt,
                    min(
                        groups[i - 1][1] + groups[i + 1][1] + 1,
                        cnt[groups[i - 1][0]]
                    )
                )

        return maxCnt


print(Solution().maxRepOpt1('ababa'))
