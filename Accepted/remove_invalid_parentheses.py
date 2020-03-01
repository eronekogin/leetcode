"""
https://leetcode.com/problems/remove-invalid-parentheses/
"""


from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        l = r = 0

        # Try to find the total misplaced left and right parentheses.
        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                if l:
                    l -= 1
                else:
                    r += 1

        rslt, n = set(), len(s)

        def do(start: int,
               lCnt: int, rCnt: int,
               lRem: int, rRem: int,
               r: List[str]):
            if start == n:  # Reaching the end of s.
                if not lRem and not rRem:  # All the misplaced are removed.
                    rslt.add(''.join(r))
            else:
                currChar = s[start]
                # Option 1: Try to discard the current parenthesis.
                if (currChar == '(' and lRem) or (currChar == ')' and rRem):
                    do(start + 1,
                        lCnt, rCnt,
                        lRem - (currChar == '('), rRem - (currChar == ')'),
                        r)

                # Option 2: Try to keep the current parenthesis.
                r.append(currChar)
                if currChar == '(':
                    do(start + 1, lCnt + 1, rCnt, lRem, rRem, r)
                elif currChar == ')':
                    # For a right parenthesis, if there is no previously
                    # unmatched left parenthesis, think it as an invalid case.
                    if lCnt > rCnt:
                        do(start + 1, lCnt, rCnt + 1, lRem, rRem, r)
                else:  # Just a normal char.
                    do(start + 1, lCnt, rCnt, lRem, rRem, r)

                # When coming here, it means it is an invalid case, just pop
                # the current char for backtracking.
                r.pop()

        do(0, 0, 0, l, r, [])
        return list(rslt)
