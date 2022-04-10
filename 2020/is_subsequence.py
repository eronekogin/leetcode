"""
https://leetcode.com/problems/is-subsequence/
"""


from bisect import bisect_left


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        start, end = 0, len(s)
        for c in t:
            if c == s[start]:
                start += 1

            if start == end:
                return True

        return False

    def isSubsequence2(self, s: str, t: str) -> bool:
        """
        Pre-processing the input t so that the check on s will be more
        efficient.

        This is a follow-up when there are multiple s as input.
        """
        if not s:
            return True

        memo = {}
        for i, c in enumerate(t):
            memo[c] = memo.get(c, []) + [i]

        currIdx = 0
        for c in s:
            if c not in memo:  # The current char cannot be found.
                return False

            idxs = memo[c]
            i = bisect_left(idxs, currIdx)
            if i == len(idxs):  # The current char cannot be found.
                return False

            currIdx = idxs[i] + 1

        return True


print(Solution().isSubsequence2('acb', 'ahbgdc'))
