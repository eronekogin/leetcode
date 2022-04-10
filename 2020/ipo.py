"""
https://leetcode.com/problems/ipo/
"""

from typing import List
from heapq import heappush, heappop


class Solution:
    def findMaximizedCapital(
            self, k: int, W: int,
            Profits: List[int], Capital: List[int]) -> int:
        """
        1. Sort the (capital, profit) pair in its reverse order so that we
            could pop the last item in O(1) time.
        2. Once the minimum capital is satisfied for a project, we add its
            pure profit to a heap.
        3. After we have collected all the satisfied projects, we choose the
            one with the maximum profit.
        4. Notice that we have to select k DISTINCT project, so we don't need
            to check the projects that has been already added to the heap. In
            other word, before adding a project to the heap, we pop it out from
            the availableProjects list.
        """
        currProfits = []
        availableProjects = sorted(zip(Capital, Profits), reverse=True)
        currCapital = W
        for _ in range(k):
            while availableProjects and\
                    availableProjects[-1][0] <= currCapital:
                heappush(currProfits, -availableProjects.pop()[1])

            if currProfits:
                currCapital -= heappop(currProfits)

        return currCapital
