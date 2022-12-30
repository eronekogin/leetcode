"""
https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
"""


from collections import deque


class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        queue = deque(students)
        currIndex = 0
        while (
            len(set(queue)) > 1 or
            (queue and queue[0] == sandwiches[currIndex])
        ):
            student = queue.popleft()
            if student == sandwiches[currIndex]:
                currIndex += 1
            else:
                queue.append(student)

        return len(queue)


print(Solution().countStudents(students=[1, 1, 0, 0], sandwiches=[0, 1, 0, 1]))
