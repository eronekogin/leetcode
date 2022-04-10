"""
https://leetcode.com/problems/reorganize-string/
"""


from heapq import heappush, heappop, heapify


from collections import Counter


class Solution:
    def reorganizeString(self, S: str) -> str:
        h = [(-cnt, c) for c, cnt in Counter(S).items()]
        heapify(h)
        rslt = []
        while h:
            cnt, c = heappop(h)
            requiredSeps = -cnt - 1
            while h and -h[0][0] <= requiredSeps:
                sepCnt, sep = heappop(h)
                rslt.extend([c, sep] * -sepCnt)
                requiredSeps += sepCnt

            if not h and requiredSeps:  # Not enough remaining separators.
                return ''

            if requiredSeps:  # Still require more separators.
                sepCnt, sep = heappop(h)
                rslt.extend([c, sep] * requiredSeps)
                heappush(h, (sepCnt + requiredSeps, sep))

            rslt.append(c)  # Append the last char.

        return ''.join(rslt)


print(Solution().reorganizeString('eqmeyggvp'))
