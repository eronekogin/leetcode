"""
https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/
"""


from heapq import heappush, heappop


class Solution:
    def minCost(self, maxTime: int, edges: list[list[int]], passingFees: list[int]) -> int:
        """
        Djikstra. And we need to consider paths that cost more fee but take less time to travel.
        """
        N = len(passingFees)

        graph = [[] for _ in range(N)]
        for x, y, t in edges:
            graph[x].append((y, t))
            graph[y].append((x, t))
        
        times = {}

        heap = [(passingFees[0], 0, 0)]
        while heap:
            currFee, currNode, currTime = heappop(heap)

            if currTime > maxTime:
                continue

            if currNode == N - 1:
                return currFee

            if currNode not in times or times[currNode] > currTime:
                times[currNode] = currTime
                for nextNode, timeCost in graph[currNode]:
                    heappush(heap, (currFee + passingFees[nextNode], nextNode, currTime + timeCost))
        
        return -1

        
        

print(Solution().minCost(29, [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], [5,1,2,20,20,3]))