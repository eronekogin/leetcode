"""
https://leetcode.com/problems/maximum-number-of-robots-within-budget/description/
"""


from collections import deque


class Solution:
    """
    Solution
    """

    def maximum_robots(self, charge_times: list[int], running_costs: list[int], budget: int) -> int:
        """
        maximum robots
        """
        start = 0
        cost = 0
        max_queue = deque()
        for end, v in enumerate(running_costs):
            cost += v

            while max_queue and charge_times[max_queue[-1]] <= charge_times[end]:
                max_queue.pop()

            max_queue.append(end)

            if charge_times[max_queue[0]] + (end - start + 1) * cost > budget:
                if max_queue[0] == start:
                    max_queue.popleft()

                cost -= running_costs[start]
                start += 1

        return len(charge_times) - start
