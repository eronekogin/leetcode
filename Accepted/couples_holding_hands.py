"""
https://leetcode.com/problems/couples-holding-hands/
"""


from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        """
        1. Solution to N integer problem: If we have a random permutation of
            N integers from 1 to N, what is the minimum swap times we need to
            make the list sorted in ascending order?
            1.1 Our goal is for each index i, i = row[i].
            1.2 If we draw an edge from the row's index to the row's actual
                value, evetually we will form a few disjoint cycles. For
                example:
                index: 0 1 2 3
                list:  3 2 0 1
                Then our cycle will be 0 -> 3 -> 1 -> 2.
            1.3 For each cycle, the minimum number of swap times is the number
                of non-self connected edge - 1. So that after those swaps, 
                each node in the cycle becomes self connected.
            1.4 We could simply start at any index i0 and eventually after
                following all the nodes in the cycle we will back to i0. If we
                are back to i0, it means we have solved all the nodes inside
                this cycle, then we could start to look at the indexes in 
                other cycles.
        2. Then we could apply the same idea as the above for this N coupling
            problem.
            2.1 Our goal now becomes that for each index i,
                i = partners[positions[partners[row[i]]]]
            2.2 Suppose the seat number is i, then the person is row[i], the
                partner for this person is partners[row[i]]. The seat number
                for this partner is positions[partners[row[i]]]. Then the
                partner of this seat number is
                partners[positions[partners[row[i]]]]. If it is different than
                i, we should swap it with i.
            2.3 We should not only swap the row but also swap the positions
                list.
        """
        N = len(row)
        swapCnt = 0
        positions, partners = [None] * N, [None] * N
        for i, v in enumerate(row):
            partners[i] = i ^ 1
            positions[v] = i

        for curr in range(N):
            expected = partners[positions[partners[row[curr]]]]
            while expected != curr:
                row[curr], row[expected] = row[expected], row[curr]
                positions[row[curr]], positions[row[expected]] = (
                    positions[row[expected]], positions[row[curr]])
                swapCnt += 1
                expected = partners[positions[partners[row[curr]]]]

        return swapCnt
