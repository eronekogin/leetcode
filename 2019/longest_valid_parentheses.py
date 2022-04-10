"""
https://leetcode.com/problems/longest-valid-parentheses/
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        workStack = [-1]  # Push -1 first to the stack to avoid boundary issue.
        maxLen = 0

        for i, c in enumerate(s):
            if c == '(':
                workStack.append(i)
            else:
                workStack.pop()  # Pop out the top element first.
                if workStack:  # Stack is not empty.
                    maxLen = max(maxLen, i - workStack[-1])
                else:
                    workStack.append(i)

        return maxLen

    def longestValidParentheses2(self, s: str) -> int:
        lCnt = rCnt = maxLen = 0
        for c in s:  # Scan from left to right.
            if c == '(':
                lCnt += 1
            else:
                rCnt += 1

            if lCnt < rCnt:
                lCnt = rCnt = 0
            elif lCnt == rCnt:
                maxLen = max(maxLen, rCnt << 1)  # rCnt * 2.

        lCnt = rCnt = 0
        for c in s[-1::-1]:  # Scan from right to left.
            if c == '(':
                lCnt += 1
            else:
                rCnt += 1

            if rCnt < lCnt:
                lCnt = rCnt = 0
            elif lCnt == rCnt:
                maxLen = max(maxLen, lCnt << 1)  # lCnt * 2.

        return maxLen


sList = ['(()', ')()())', ')(()()))', "()(()", ')(']
solution = Solution()
for s in sList:
    print(solution.longestValidParentheses2(s))
