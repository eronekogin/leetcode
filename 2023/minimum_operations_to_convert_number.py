"""
https://leetcode.com/problems/minimum-operations-to-convert-number/
"""

from collections import deque


class Solution:
    """
    Solution
    """

    def minimum_operations(self, nums: list[int], start: int, goal: int) -> int:
        """
        minimum_operations
        """
        def bfs(nums: list[int]):
            visited = {start}
            queue: deque[tuple[int, int]] = deque([(0, start)])
            while queue:
                curr_steps, curr_num = queue.popleft()
                for x in nums:
                    for next_num in (curr_num + x, curr_num - x, curr_num ^ x):
                        if next_num == goal:
                            return curr_steps + 1

                        if next_num not in visited and 0 <= next_num <= 1000:
                            visited.add(next_num)
                            queue.append((curr_steps + 1, next_num))

            return -1  # Not possible

        # Filter nums first to get candidates.
        candidates: list[int] = []
        for x in nums:
            if not (
                (x <= 0 or x > 1000) and
                (goal - x < 0 or goal - x > 1000) and
                (goal + x < 0 or goal + x > 1000) and
                (goal ^ x < 0 or goal ^ x > 1000)
            ):
                candidates.append(x)

        return bfs(candidates)
