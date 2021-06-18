"""
https://leetcode.com/problems/reverse-only-letters/
"""


from string import ascii_letters


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        MEMO = set(ascii_letters)
        start, end = 0, len(s) - 1
        rslt = list(s)
        while start < end:
            while start < end and rslt[start] not in MEMO:
                start += 1

            while start < end and rslt[end] not in MEMO:
                end -= 1

            rslt[start], rslt[end] = rslt[end], rslt[start]
            start += 1
            end -= 1

        return ''.join(rslt)


print(Solution().reverseOnlyLetters('a-bC-dEf-ghIj'))
