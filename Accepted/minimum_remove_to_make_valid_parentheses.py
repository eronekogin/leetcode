"""
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        For any prefix in a valid string with parentheses, its left parentheses
        should be no less than its right parentheses, same as suffix. So we
        could scan from left to right to remove invalid right parentheses, then
        scan from right to left to remove invalid left parentheses.
        """
        rslt, N = list(s), len(s)
        leftCnt = rightCnt = 0
        for i in range(N):  # From left to right.
            if rslt[i] == '(':
                leftCnt += 1
            elif rslt[i] == ')':
                rightCnt += 1
                if leftCnt < rightCnt:
                    rslt[i] = ''
                    rightCnt -= 1

        leftCnt = rightCnt = 0
        for i in reversed(range(N)):  # From right to left.
            if rslt[i] == ')':
                rightCnt += 1
            elif rslt[i] == '(':
                leftCnt += 1
                if rightCnt < leftCnt:
                    rslt[i] = ''
                    leftCnt -= 1

        return ''.join(rslt)


print(Solution().minRemoveToMakeValid('(a(b(c)d)'))
