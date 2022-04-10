"""
https://leetcode.com/problems/unique-substrings-in-wraparound-string/
"""


class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        if not p:  # Empty p.
            return 0

        # Each element indicate the length of the longest string in p that
        # ends with a specific char which is from a to z.
        memo = [0] * 26
        currMaxLen, offset = 1, ord('a')
        memo[ord(p[0]) - offset] = 1
        for i in range(1, len(p)):
            im, chk = ord(p[i]) - offset, ord(p[i]) - ord(p[i - 1])
            if chk == 1 or chk == -25:  # abcd... or xyzabc...
                currMaxLen += 1
            else:  # Found a new end.
                currMaxLen = 1

            memo[im] = max(memo[im], currMaxLen)

        return sum(memo)


print(Solution().findSubstringInWraproundString('zab'))
