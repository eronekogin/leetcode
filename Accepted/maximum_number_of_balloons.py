"""
https://leetcode.com/problems/maximum-number-of-balloons/
"""


from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        TARGET = 'balloon'
        remainChars = Counter(text)
        cnt = 0
        found = True
        while found:
            for c in TARGET:
                if remainChars[c] == 0:
                    found = False
                    break
                else:
                    remainChars[c] -= 1

            if found:
                cnt += 1

        return cnt
