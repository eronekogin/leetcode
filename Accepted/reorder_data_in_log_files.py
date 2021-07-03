"""
https://leetcode.com/problems/reorder-data-in-log-files/
"""


class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        def genKey(s: str) -> tuple[str]:
            w, remainLog = s.split(' ', maxsplit=1)
            if remainLog[0].isalpha():
                return (0, remainLog, w)
            else:
                return (1, )

        return sorted(logs, key=genKey)
