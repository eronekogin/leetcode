"""
https://leetcode.com/problems/minimum-number-of-frogs-croaking/
"""


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        frogs = c = r = o = a = k = 0
        for ch in croakOfFrogs:
            if ch == 'c':
                c += 1
                frogs = max(frogs, c - k)
            elif ch == 'r':
                r += 1
            elif ch == 'o':
                o += 1
            elif ch == 'a':
                a += 1
            else:
                k += 1

            if not c >= r >= o >= a >= k:  # Must increase monotonically.
                return -1

        if c == k:  # Each c must have a closing k.
            return frogs

        return -1


print(Solution().minNumberOfFrogs("aoocrrackk"))
