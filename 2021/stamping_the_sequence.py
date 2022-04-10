"""
https://leetcode.com/problems/stamping-the-sequence/
"""


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> list[int]:
        """
        Do the stamp in a reverse way, which try to match the full stamp first,
        then for each mapping window, mark them with '?'. For example:
            stamp = abc, target = ababc

            1. i = 2, target = ab???, rslt = [2]
            2. i = 0, target = ?????, rslt = [2, 0]
            3. Then no changes on this round, rslt[::-1] is the right way
                to stamp on the original string.
        """
        def could_stamp(start: int) -> bool:
            changed = False
            for offset in range(sLen):
                if t[start + offset] != '?':
                    if t[start + offset] != s[offset]:  # Cannot match.
                        return False

                    changed = True

            if changed:
                t[start: start + sLen] = marks
                rslt.append(start)

            return changed

        tLen, sLen = len(target), len(stamp)
        t, s = list(target), list(stamp)
        rslt = []
        marks = ['?'] * sLen

        changed = True
        while changed:
            changed = False
            for start in range(tLen - sLen + 1):
                # Using bitwise or is much faster than using logical or in
                # this case.
                changed |= could_stamp(start)

        if t == ['?'] * tLen:
            return rslt[::-1]

        return []


print(Solution().movesToStamp('abc', 'ababc'))
