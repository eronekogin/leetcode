"""
https://leetcode.com/problems/jump-game-iii/
"""


from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def move(currIdx: int) -> bool:
            if currIdx >= 0 and currIdx < n and not visited[currIdx]:
                if not arr[currIdx]:
                    return True

                visited[currIdx] = True
                return move(currIdx + arr[currIdx]) or \
                    move(currIdx - arr[currIdx])

            return False

        n = len(arr)
        visited = [False] * n
        return move(start)


print(Solution().canReach([3, 0, 2, 1, 2], 2))
