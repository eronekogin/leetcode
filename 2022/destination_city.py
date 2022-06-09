"""
https://leetcode.com/problems/destination-city/
"""


class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        srcs: set[str] = set()
        dests: set[str] = set()
        for src, dest in paths:
            srcs.add(src)
            dests.add(dest)

        for dest in dests:
            if dest not in srcs:
                return dest
