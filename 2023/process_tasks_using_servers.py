"""
https://leetcode.com/problems/process-tasks-using-servers/
"""


from heapq import heappush, heappop, heapify
from collections import deque


class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        freeServers = [(w, i) for i, w in enumerate(servers)]
        heapify(freeServers)

        rslt = [0] * len(tasks)
        busyServers = []
        pendingTasks = deque([])
        for currTime, executionTime in enumerate(tasks):
            while busyServers and busyServers[0][0] <= currTime:
                _, w, i = heappop(busyServers)
                heappush(freeServers, (w, i))
            
            while freeServers and pendingTasks:
                prevTime, prevExecutionTime = pendingTasks.popleft()
                w, i = heappop(freeServers)
                rslt[prevTime] = i
                heappush(busyServers, (currTime + prevExecutionTime, w, i))
            
            if freeServers:
                w, i = heappop(freeServers)
                rslt[currTime] = i
                heappush(busyServers, (currTime + executionTime, w, i))
            else:
                pendingTasks.append((currTime, executionTime))
        
        while pendingTasks:
            prevTime, prevExecutionTime = pendingTasks.popleft()
            currTime, w, i = heappop(busyServers)
            rslt[prevTime] = i
            heappush(busyServers, (currTime + prevExecutionTime, w, i))
        
        return rslt
    
print(Solution().assignTasks([10,63,95,16,85,57,83,95,6,29,71], [70,31,83,15,32,67,98,65,56,48,38,90,5]))






