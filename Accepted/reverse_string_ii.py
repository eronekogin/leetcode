"""
https://leetcode.com/problems/reverse-string-ii/
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        rslt, n = list(s), len(s)
        needReverse = True
        for i in range(0, n, k):
            if needReverse:
                l, r = i, min(i + k - 1, n - 1)
                while l < r:
                    rslt[l], rslt[r] = rslt[r], rslt[l]
                    l += 1
                    r -= 1

            needReverse = not needReverse

        return ''.join(rslt)

    def reverseStr2(self, s: str, k: int) -> str:
        rslt = list(s)
        for i in range(0, len(s), k << 1):
            rslt[i: i + k] = reversed(rslt[i: i + k])

        return ''.join(rslt)
