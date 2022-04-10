"""
https://leetcode.com/problems/remove-k-digits/
"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:  # Remove all.
            return '0'

        stack = []
        charsToRemove = k
        for c in num:
            while stack and stack[-1] > c and charsToRemove > 0:
                stack.pop()
                charsToRemove -= 1

            stack.append(c)

        # For case like 453219 or 111111.
        while charsToRemove > 0:
            stack.pop()
            charsToRemove -= 1

        rslt = ''.join(stack).lstrip('0')
        return rslt if rslt else '0'


print(Solution().removeKdigits('453210', 5))
