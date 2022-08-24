"""
https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/
"""


class Solution:
    def minInsertions(self, s: str) -> int:
        insertCnt = 0
        requiredRightParenthesisCnt = 0
        for c in s:
            if c == ')':
                requiredRightParenthesisCnt -= 1
                if requiredRightParenthesisCnt < 0:
                    # Not enough left parenthesis, eg: ()))
                    insertCnt += 1  # Add a left parenthesis
                    requiredRightParenthesisCnt += 2
            else:
                if requiredRightParenthesisCnt & 1:
                    # Odd right parenthesis before the current left
                    # parenthesis. eg: ()())
                    insertCnt += 1  # Add a right parenthesis
                    requiredRightParenthesisCnt -= 1

                # A left parenthesis needs two right parenthesis.
                requiredRightParenthesisCnt += 2

        return insertCnt + requiredRightParenthesisCnt
