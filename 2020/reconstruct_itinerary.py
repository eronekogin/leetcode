"""
https://leetcode.com/problems/reconstruct-itinerary/
"""


from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        memo = {}
        for dpt, arr in reversed(sorted(tickets)):
            # Generate memo, need to keep lexico order.
            memo[dpt] = memo.get(dpt, []) + [arr]

        route, stack = [], ['JFK']
        while stack:
            # Simply go straight forward until no more arrival airport
            # from the current departing airport.
            while memo.get(stack[-1]):
                stack.append(memo[stack[-1]].pop())

            # Mark the stcuked node as the end point. Then go back
            # to look for the other paths.
            route.append(stack.pop())

        return route[::-1]


print(Solution().findItinerary(
    [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
