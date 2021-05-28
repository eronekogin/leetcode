"""
https://leetcode.com/problems/find-and-replace-pattern/
"""


class Solution:
    def findAndReplacePattern(
            self, words: list[str], pattern: str) -> list[str]:
        def match(w: str) -> bool:
            memo = {}
            for x, y in zip(pattern, w):
                if memo.setdefault(x, y) != y:
                    # x is set with another value before.
                    return False

            # Make sure each mapped value only occurrs once.
            return len(set(memo.values())) == len(memo.values())

        return [w for w in words if match(w)]
