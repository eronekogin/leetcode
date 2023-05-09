"""
https://leetcode.com/problems/single-threaded-cpu/
"""


from heapq import heappush, heappop


class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        taskHeap = []
        for i, (et, pt) in enumerate(tasks):
            heappush(taskHeap, (et, pt, i))

        processHeap = []
        rslt = []
        nextPickTime = taskHeap[0][0]
        while taskHeap:
            # Collect available tasks before the next cpu pick time.
            while taskHeap and taskHeap[0][0] <= nextPickTime:
                task = heappop(taskHeap)
                heappush(processHeap, (task[1], task[2]))

            # Pick the next task.
            if not processHeap:  # No available tasks yet.
                if taskHeap:  # Still has more tasks to enque.
                    nextPickTime = taskHeap[0][0]
            else:
                t, i = heappop(processHeap)
                rslt.append(i)
                nextPickTime += t

        # Process remaining tasks.
        while processHeap:
            rslt.append(heappop(processHeap)[1])

        return rslt


print(Solution().getOrder([[5, 2], [7, 2], [9, 4], [6, 3], [5, 10], [1, 1]]))
