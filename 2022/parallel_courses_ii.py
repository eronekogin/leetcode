"""
https://leetcode.com/problems/parallel-courses-ii/
"""


from functools import lru_cache
from collections import defaultdict
from itertools import combinations


class Solution:
    def minNumberOfSemesters(
        self,
        n: int,
        relations: list[list[int]],
        k: int
    ) -> int:
        @lru_cache(None)
        def dp(prevTakenCoursesMask: int) -> int:
            if prevTakenCoursesMask == ALL_COURSE_TAKEN_MASK:
                return 0

            candidateCourses: list[int] = []
            for i in range(n):
                if not prevTakenCoursesMask & (1 << i) and degrees[i] == 0:
                    candidateCourses.append(i)

            minSemester = float('inf')
            for pickedCourses in combinations(
                candidateCourses, min(k, len(candidateCourses))
            ):
                newMask = prevTakenCoursesMask
                for course in pickedCourses:
                    newMask |= (1 << course)
                    for nextCourse in courseDependencies[course]:
                        degrees[nextCourse] -= 1

                minSemester = min(minSemester, 1 + dp(newMask))

                # Restore degrees.
                for course in pickedCourses:
                    for nextCourse in courseDependencies[course]:
                        degrees[nextCourse] += 1

            return minSemester

        ALL_COURSE_TAKEN_MASK = (1 << n) - 1
        degrees = [0] * n
        courseDependencies = defaultdict(set)

        # Initialize dependencies.
        for prevCourse, nextCourse in relations:
            courseDependencies[prevCourse - 1].add(nextCourse - 1)
            degrees[nextCourse - 1] += 1

        return dp(0)
