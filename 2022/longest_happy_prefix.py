"""
https://leetcode.com/problems/longest-happy-prefix/
"""


class Solution:
    def longestPrefix(self, s: str) -> str:
        """
        Brutal force.
        """
        N = len(s)
        candidateSuffixStarts = []
        for i in range(1, N):
            if s[i] == s[0]:
                candidateSuffixStarts.append(i)

        maxLen = 0
        for start in candidateSuffixStarts:
            if s[:N - start] == s[start:]:
                if N - start > maxLen:
                    maxLen = N - start

        return s[:maxLen]

    def longestPrefix2(self, s: str) -> str:
        """
        Rolling hash:
            1. Calculate hash value for both prefix and suffix.
            2. When the hash values are equal, it means we find a match.
            3. For hash collision, since s only contains lower english letters,
                at least the expotential should be larger than 26, here we
                use 128 as that is the total number of ascii letters.
            4. Then in order to prevent a very large hash value, use mod to
                10**9 + 7 instead.
        """
        N = len(s)
        maxLen = 0
        hl = hr = 0
        p, m, e = 1, 10 ** 9 + 7, 128

        for i in range(N - 1):
            hl = (hl * e + ord(s[i])) % m
            hr = (hr + p * ord(s[N - 1 - i])) % m
            if hl == hr:
                maxLen = i + 1

            p = (p * e) % m

        return s[:maxLen]


print(Solution().longestPrefix('babbb'))
