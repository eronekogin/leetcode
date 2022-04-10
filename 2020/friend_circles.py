"""
https://leetcode.com/problems/friend-circles/
"""


from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def check_friends(student: int) -> None:
            for friend, isFriend in enumerate(M[student]):
                if isFriend and friend not in visited:
                    visited.add(friend)
                    check_friends(friend)

        circles, visited = 0, set()
        for student in range(len(M)):
            if student not in visited:  # Found the start of a new circle.
                circles += 1
                visited.add(student)
                check_friends(student)

        return circles


print(Solution().findCircleNum(
    [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]))
