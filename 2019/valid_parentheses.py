"""
https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    def isValid(self, s: 'str') -> 'bool':
        workStack = []
        refDict = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in refDict:  # New close bracket.
                if workStack:
                    chkChar = workStack.pop()
                else:  # Stack is empty.
                    chkChar = None

                if chkChar != refDict[c]:
                    return False  # No matching open bracket.
            else:  # New open bracket.
                workStack.append(c)  # Simply push it to stack.

        return not workStack
