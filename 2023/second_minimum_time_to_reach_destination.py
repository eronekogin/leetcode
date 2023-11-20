"""
https://leetcode.com/problems/second-minimum-time-to-reach-destination/
"""


from collections import deque


class Solution:
    """
    Solution
    """

    def second_minimum(self, n: int, edges: list[list[int]], time: int, change: int) -> int:
        """
        second_minimum
        """
        graph = [[] for _ in range(n)]
        for curr_node, next_node in edges:
            graph[curr_node - 1].append(next_node - 1)
            graph[next_node - 1].append(curr_node - 1)

        least = None
        queue: deque[tuple[int, int]] = deque([(0, 0)])
        seen = [[] for _ in range(n)]
        while queue:
            curr_time, curr_node = queue.popleft()
            if curr_node == n - 1:
                if least is None:
                    least = curr_time
                elif least < curr_time:
                    return curr_time

            if (curr_time // change) & 1:
                # waiting for green.
                curr_time = (curr_time // change + 1) * change

            curr_time += time

            for next_node in graph[curr_node]:
                if (
                    not seen[next_node] or
                    (
                        len(seen[next_node]) == 1 and
                        seen[next_node][0] != curr_time
                    )
                ):
                    seen[next_node].append(curr_time)
                    queue.append((curr_time, next_node))

        return -1  # Not possible to reach node n
