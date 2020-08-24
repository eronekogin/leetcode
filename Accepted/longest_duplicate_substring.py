"""
https://leetcode.com/problems/longest-duplicate-substring/
"""


from collections import defaultdict


class Solution:
    def longestDupSubstring(self, S: str) -> str:

        def check_dup_with_k_length(k: int) -> str:
            MOD = (1 << 61) - 1  # Pick a large prime as mod.
            BASE = 26
            HIGHEST_WEIGHT = pow(BASE, k - 1, MOD)
            currHash = 0
            visited = defaultdict(list)
            for i, c in enumerate(S):
                if i >= k:
                    # Get rid of the first char in
                    # the current window.
                    firstCharVal = ord(S[i - k]) - ord('a')
                    currHash = (
                        currHash - firstCharVal * HIGHEST_WEIGHT) % MOD

                currCharVal = ord(c) - ord('a')
                currHash = (currHash * BASE + currCharVal) % MOD

                if i >= k - 1:
                    chkStr = S[i - k + 1: i + 1]
                    for j in visited[currHash]:
                        # If found the same hash in the previous
                        # visited strings, check if it is the same string.
                        if S[j - k + 1: j + 1] == chkStr:  # Found dup.
                            return chkStr

                    visited[currHash].append(i)

        l, r = 2, len(S) - 1
        rslt = ''
        while l <= r:
            m = l + ((r - l) >> 1)
            candidate = check_dup_with_k_length(m)
            if candidate:
                rslt = candidate
                l = m + 1  # Try to find longer sub string.
            else:
                r = m - 1  # No dup found, try to search for smaller string.

        return rslt
