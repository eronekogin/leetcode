"""
https://leetcode.com/problems/letter-case-permutation/
"""


class Solution:
    def letterCasePermutation(self, S: str) -> list[str]:
        if S[0].isdigit():
            currLevel = [S[0]]
        else:
            currLevel = [S[0].lower(), S[0].upper()]

        for i in range(1, len(S)):
            c = S[i]
            if c.isdigit():
                nextLevel = [s + c for s in currLevel]
            else:
                smallLetter, capitalLetter = c.lower(), c.upper()
                nextLevel = [s + smallLetter for s in currLevel]
                nextLevel += [s + capitalLetter for s in currLevel]

            currLevel = nextLevel

        return currLevel


print(Solution().letterCasePermutation('a1b2'))
