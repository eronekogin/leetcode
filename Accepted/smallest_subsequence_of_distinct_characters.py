"""
https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
"""


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        lastIndexes = {c: i for i, c in enumerate(s)}
        stack = []
        for i, c in enumerate(s):
            if c not in stack:
                while stack and stack[-1] > c and i < lastIndexes[stack[-1]]:
                    stack.pop()

                stack.append(c)

        return ''.join(stack)
