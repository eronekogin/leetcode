"""
https://leetcode.com/problems/replace-the-substring-for-balanced-string/
"""


from collections import Counter


class Solution:
    def balancedString(self, s: str) -> int:
        """
        Using sliding window, check the total occurrences of QWER outside
        of the current sliding window to see if there are enough QWER. Then
        we could always replace the chars within the current window to
        make the string balanced.
        """
        VALID_CHARS = 'QWER'
        N = len(s)
        MAX_FREQ = N // 4
        freqs = Counter(s)
        minLen = N
        start = 0
        for end, c in enumerate(s):
            freqs[c] -= 1
            while start < N and all(MAX_FREQ >= freqs[c] for c in VALID_CHARS):
                minLen = min(minLen, end - start + 1)
                freqs[s[start]] += 1
                start += 1

        return minLen


print(Solution().balancedString('QQQW'))
