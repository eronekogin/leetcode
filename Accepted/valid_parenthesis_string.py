"""
https://leetcode.com/problems/valid-parenthesis-string/
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        minOpenLeft = maxOpenLeft = 0
        for c in s:
            if c == '(':
                minOpenLeft += 1
                maxOpenLeft += 1
            elif c == ')':
                minOpenLeft -= 1
                maxOpenLeft -= 1
            else:
                minOpenLeft -= 1
                maxOpenLeft += 1

            if maxOpenLeft < 0:
                return False

            # Ignore the cases when minOpenLeft < 0 as
            # the left parenthesis must go before the right one.
            minOpenLeft = max(0, minOpenLeft)

        return not minOpenLeft
