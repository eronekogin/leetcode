"""
https://leetcode.com/problems/combination-sum-iii/
"""


from typing import List
from collections import deque


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k > 9:  # Invalid k.
            return []

        # n > (9 - k + 1 + 9) * k // 2
        if n < (k * (k + 1)) // 2 or n > k * (19 - k) // 2:  # Invalid n.
            return []

        rslt = []
        queue = deque(
            [
                [i]
                for i in range(1, 10)
                if n >= (k + 2 * i - 1) * k // 2
            ])  # (i + k - 1 + i) * k // 2

        while queue:
            currPath = queue.popleft()
            sumRemain, selectStart = n - sum(currPath), currPath[-1] + 1
            if len(currPath) == k - 1:
                if 9 >= sumRemain >= selectStart:
                    rslt.append(currPath + [sumRemain])
            else:
                # sumRemain - selectStart > selectStart
                while sumRemain > selectStart * 2:
                    queue.append(currPath + [selectStart])
                    selectStart += 1

        return rslt


print(Solution().combinationSum3(3, 7))
