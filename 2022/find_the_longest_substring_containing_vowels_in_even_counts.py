"""
https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/
"""


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        memo = {c: i for i, c in enumerate('aeiou')}
        seen = {0: -1}  # Store the first occurring index of mask.
        maxLen = 0
        currMask = 0
        for i, c in enumerate(s):
            if c in memo:  # Only change mask when the char is a vowel.
                currMask ^= 1 << memo[c]
                seen.setdefault(currMask, i)

            # If the same mask occurs again, it means the chars in the
            # middle has even number of vowels, in other words:
            # currMask ^ currMask = 0.
            maxLen = max(maxLen, i - seen[currMask])

        return maxLen


print(Solution().findTheLongestSubstring(
    "eleetminicoworoep"))
