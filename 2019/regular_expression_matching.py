"""
https://leetcode.com/problems/regular-expression-matching/
"""


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}
        sLen = len(s)
        pLen = len(p)

        # Use recursive here to clearly describe the dynamic planning.
        def dp(idxS, idxP):
            matchRslt = memo.get((idxS, idxP))

            if matchRslt is None:
                if idxP == pLen:
                    """
                    When the pattern check reaches its end, the only
                    match case is when the string check reaches its end
                    as well.
                    """
                    matchRslt = idxS == sLen
                else:
                    """
                    Check if the current pattern char at idxP == the current
                    string char at idxS. A single '.' could match any char
                    in the string.
                    """
                    firstMatch = idxS < sLen and p[idxP] in {s[idxS], '.'}

                    if idxP + 1 < pLen and p[idxP + 1] == '*':
                        """
                        When the current pattern char is followed by a 
                        '*', we could take two roads as the next action:

                          1. Ignore the current matching, means a* is an empty
                             string.
                          2. Take the current matching and continue to check
                             the next char in the string.
                        """
                        matchRslt = dp(idxS, idxP + 2) or \
                            (firstMatch and dp(idxS + 1, idxP))
                    else:
                        # Continue to check the next char if no '*' occurrs.
                        matchRslt = firstMatch and dp(idxS + 1, idxP + 1)

                memo[(idxS, idxP)] = matchRslt  # Save middle results to memo.

            return matchRslt

        return dp(0, 0)


sol = Solution()
s, p = 'aaa', 'ab*a*c*a'

print(sol.isMatch(s, p))
