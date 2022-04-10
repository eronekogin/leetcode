"""
https://leetcode.com/problems/minimum-window-substring/
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        r, n = 0, len(s)
        rslt = (n + 1, 0)  # Current sub string length and its start position.

        # Generate counter check dictionary.
        chkDict = {}
        for c in t:
            chkDict[c] = chkDict.get(c, 0) + 1

        cntDict, posList = {}, []
        posIndex = matchedCnt = posMax = 0
        requiredCnt = len(chkDict)
        while r < n:
            c = s[r]
            if c in chkDict:
                cntDict[c] = cntDict.get(c, 0) + 1
                posList.append(r)
                posMax += 1
                if cntDict[c] == chkDict[c]:
                    matchedCnt += 1

                # Try to contract the current window when found a satisfied
                # sub string in order to get the shortest one based on the
                # current window.
                while matchedCnt == requiredCnt and posIndex < posMax:
                    l = posList[posIndex]
                    c = s[l]
                    cntDict[c] -= 1
                    if cntDict[c] < chkDict[c]:
                        matchedCnt -= 1
                        # Found the shortest sub string in the current window.
                        currLen = r - l + 1
                        if currLen < rslt[0]:
                            rslt = (currLen, l)

                    posIndex += 1

            # Expand r to find new sub string.
            r += 1

        if rslt[0] > n:
            return ''
        else:
            return s[rslt[1]: rslt[1] + rslt[0]]


s, t = "A", "A"
print(Solution().minWindow(s, t))
