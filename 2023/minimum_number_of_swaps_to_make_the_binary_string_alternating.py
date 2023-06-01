"""
https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/
"""


class Solution:
    def minSwaps(self, s: str) -> int:
        def count_swaps(target: str):
            wrongChars = 0
            for c in s:
                if c != target:
                    wrongChars += 1

                target = '1' if target == '0' else '0'

            return wrongChars >> 1

        ones = s.count('1')
        zeros = len(s) - ones

        if abs(ones - zeros) > 1:
            return -1

        if ones > zeros:
            return count_swaps('1')

        if zeros > ones:
            return count_swaps('0')

        return min(
            count_swaps('0'),
            count_swaps('1')
        )
