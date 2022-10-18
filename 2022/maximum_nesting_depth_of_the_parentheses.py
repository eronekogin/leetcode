"""
https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
"""


class Solution:
    def maxDepth(self, s: str) -> int:
        nestedDepth = currDepth = 0
        for c in s:
            if c == '(':
                currDepth += 1
            elif c == ')':
                nestedDepth = max(nestedDepth, currDepth)
                currDepth -= 1

        return nestedDepth
