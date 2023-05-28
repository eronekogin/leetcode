"""
https://leetcode.com/problems/incremental-memory-leak/
"""


class Solution:
    def memLeak(self, memory1: int, memory2: int) -> list[int]:
        rslt = [1, memory1, memory2]
        while True:
            if rslt[2] > rslt[1]:
                i = 2
            else:
                i = 1

            if rslt[0] > rslt[i]:
                return rslt

            rslt[i] -= rslt[0]
            rslt[0] += 1
