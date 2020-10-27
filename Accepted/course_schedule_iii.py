"""
https://leetcode.com/problems/course-schedule-iii/
"""


from typing import List
from heapq import heappush, heappop


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """
        1. Sort the courses by its ending time in ascending order.
        2. Then for the first k courses, the condition to select all of them
            is their total duration <= the current largest end time for all k.
        3. Then for each k, when the above condition is not satisfied, we
            simply remove the course with the maximum duration from the
            selected course list, which will give us the maximum space to
            select the next course.
        """
        currStartTime, selected = 0, []
        for duration, endTime in sorted(courses, key=lambda x: x[-1]):
            currStartTime += duration
            heappush(selected, -duration)
            if currStartTime > endTime:
                currStartTime += heappop(selected)

        return len(selected)
