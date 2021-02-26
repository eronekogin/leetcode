"""
https://leetcode.com/problems/validate-stack-sequences/
"""


class Solution:
    def validateStackSequences(
            self, pushed: list[int], popped: list[int]) -> bool:
        """
        We already have the pushing sequence showed from the pushed list. Then
        when any item that needs to be popped is at the top of the current
        stack, it must be popped now or it will never get popped with the same
        order as popped.
        """
        popIdx = 0
        stack = []
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[popIdx]:
                stack.pop()
                popIdx += 1

        return not stack
