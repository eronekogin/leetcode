"""
https://leetcode.com/problems/find-the-winner-of-an-array-game/
"""


from collections import deque


class Solution:
    def getWinner(self, arr: list[int], k: int) -> int:
        maxNum = max(arr)
        queue = deque(arr)
        wins = 0
        while wins < k and queue[0] != maxNum:
            a = queue.popleft()
            b = queue.popleft()
            if a > b:
                queue.appendleft(a)
                queue.append(b)
                wins += 1
            else:
                queue.appendleft(b)
                queue.append(a)
                wins = 1

        return queue[0]
