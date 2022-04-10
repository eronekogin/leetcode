"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chkDict = {}
        rslt = startPos = 0

        for currPos, chkChar in enumerate(s):
            if chkChar in chkDict and startPos <= chkDict[chkChar]:
                rslt = max(rslt, currPos - startPos)
                startPos = chkDict[chkChar] + 1

            chkDict[chkChar] = currPos

        return max(rslt, len(s) - startPos)
