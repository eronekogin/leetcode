"""
https://leetcode.com/problems/increasing-decreasing-string/
"""


class Solution:
    def sortString(self, s: str) -> str:
        def append_chars(reverse: bool) -> None:
            for key in sorted(cnt.keys(), reverse=reverse):
                rslt.append(key)
                cnt[key] -= 1
                if cnt[key] == 0:
                    del cnt[key]

        rslt = []
        cnt = {}
        for c in s:
            cnt[c] = cnt.get(c, 0) + 1

        while cnt:
            append_chars(False)
            append_chars(True)

        return ''.join(rslt)
