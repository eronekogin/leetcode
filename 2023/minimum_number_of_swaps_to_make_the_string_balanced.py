"""
https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/
"""


class Solution:
    def minSwaps(self, s: str) -> int:
        """
        Remove the matched pairs as they don't impact the result, then the remaining string will looks like
            ...]]]]...[[[[...

        Then for each swap we can match two pairs, so the total swap is (mismatched + 1) // 2.
        """
        mismatched = 0
        for c in s:
            if c == '[':
                mismatched += 1
            elif mismatched > 0:
                mismatched -= 1
        
        return (mismatched + 1) >> 1