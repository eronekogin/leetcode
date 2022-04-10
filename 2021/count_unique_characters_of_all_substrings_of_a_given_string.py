"""
https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/
"""


from string import ascii_uppercase


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        """
        1. Think of s as XA(XAXX)AX, the sequence between the parentheses is
            our substring. Then in order to make A as a unique character in
            this substring, we should divide the sub string as follows:
            1.1 Around the previous A: A(XA...) or AX(A...)
            1.2 Around the next A: (...A)XXA, (...AX)XA, (...AXX)A
            So total cases will be previous * next, in the substrings generated
            in those cases, A is a unique character.
        2. Then in order to find the total unique characters in all substrings,
            we could try to find all the cases to make a single character
            unique, then sum them together to get our answer.
        """
        memo = {c: [-1, -1] for c in ascii_uppercase}
        rslt = 0
        for r, c in enumerate(s):
            l, m = memo[c]
            rslt += (r - m) * (m - l)
            memo[c] = [m, r]

        r = len(s)
        for l, m in memo.values():  # Count the tailing part.
            rslt += (r - m) * (m - l)

        return rslt % (10 ** 9 + 7)
