"""
https://leetcode.com/problems/largest-multiple-of-three/
"""


from collections import Counter


class Solution:
    def largestMultipleOfThree(self, digits: list[int]) -> str:
        """
        999....999 % 3 == 0
        1000....000 % 3 == 1
        a000....000 % 3 == a % 3
        abcdefghijk % 3 == (a+b+c+..+i+j+k) % 3 
        """
        def f(x: int) -> str:
            if cnt[x]:
                sortedDigits.remove(x)
                cnt[x] -= 1

            if not sortedDigits:
                return ''

            if not any(sortedDigits):
                return '0'

            if sum(sortedDigits) % 3 == 0:
                return ''.join(map(str, sortedDigits))

        cnt = Counter(digits)
        sortedDigits = sorted(digits, reverse=True)
        total = sum(sortedDigits)

        if total % 3 == 0:
            return f(-1)

        if total % 3 == 1 and cnt[1] + cnt[4] + cnt[7]:
            return f(1) or f(4) or f(7)

        if total % 3 == 2 and cnt[2] + cnt[5] + cnt[8]:
            return f(2) or f(5) or f(8)

        if total % 3 == 2:  # Remove two digits of 1 or 4 or 7.
            return f(1) or f(1) or f(4) or f(4) or f(7) or f(7)

        # Now total % 3 will be 1, try to remove two digits of 2, 5, 8.
        return f(2) or f(2) or f(5) or f(5) or f(8) or f(8)
