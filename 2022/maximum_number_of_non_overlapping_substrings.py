"""
https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/
"""


class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        uniqueChars = set(s)

        # Build intervals
        intervals = {
            c: (s.rindex(c), s.index(c))
            for c in uniqueChars
        }

        # Merge intervals to include all occurrences
        # of all chars in an interval.
        for c in uniqueChars:
            r, l = intervals[c]
            nl, nr = -1, -1
            while not (nl == l and nr == r):
                nl, nr = l, r
                allChars = set(s[l: r + 1])
                r = max(intervals[k][0] for k in allChars)
                l = min(intervals[k][1] for k in allChars)

            intervals[c] = (r, l)

        # Sort merged intervals by end so that we could choose the candidate
        # intervals with minimum length.
        rslt, curr = [], 0
        for r, l in sorted(intervals.values()):
            if l >= curr:
                rslt.append(s[l: r + 1])
                curr = r

        return rslt


print(Solution().maxNumOfSubstrings("adefaddaccc"))
