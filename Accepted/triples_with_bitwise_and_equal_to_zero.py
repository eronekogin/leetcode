"""
https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/
"""


from collections import Counter


class Solution:
    def countTriplets(self, nums: list[int]) -> int:
        twoNumsCnt = Counter()
        for x in nums:
            for y in nums:
                twoNumsCnt[x & y] += 1

        rslt = 0
        for z in nums:
            for xAndy, cnt in twoNumsCnt.items():
                if z & xAndy == 0:
                    rslt += cnt

        return rslt
