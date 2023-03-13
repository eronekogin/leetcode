"""
https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/
"""


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        found = False
        i, n = 0, len(s)
        while i < n:
            if s[i] == '1':
                if found:
                    return False

                while i < n and s[i] == '1':
                    i += 1

                found = True
            else:
                i += 1

        return found


print(Solution().checkOnesSegment('110'))
