"""
https://leetcode.com/problems/maximum-length-of-pair-chain/
"""


from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        """
        After sort the pairs by the second item in each pair, we can conclude
        that it is always better to add a pair with smaller second item to the
        current chain than to add a pair with larger one as follows:
        1. Suppose pa[1] < pb[1].
        2. If pb[0] > pa[1], we should add pa to the chain first.
        3. Else, we can add either pa or pb. And after adding either pa or pb,
            then current chain's end will be either pa[1] or pb[1].
        4. Since pa[1] < pb[1], if we add pa to the chain, we will have a
            better chance than adding pb to the chain in order to get a longer
            chain.
        """
        currEnd, cnt = float('-inf'), 0
        for start, end in sorted(pairs, key=lambda x: x[1]):
            if currEnd < start:
                currEnd = end
                cnt += 1

        return cnt


print(Solution().findLongestChain(
    [[-6, 9], [1, 6], [8, 10], [-1, 4], [-6, -2], [-9, 8], [-5, 3], [0, 3]]))
