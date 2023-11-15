"""
https://leetcode.com/problems/the-time-when-the-network-becomes-idle/
"""


from collections import defaultdict, deque


class Solution:
    """
    Solution
    """

    def network_becomes_idle(self, edges: list[list[int]], patience: list[int]) -> int:
        """
        network_becomes_idle
        """
        # Build graph.
        graph: defaultdict[int, list[int]] = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Use bfs to get the minimum time from master node to each data node.
        queue = deque([0])
        n = len(patience)
        min_times = [-1] * n
        min_times[0] = 0
        while queue:
            curr_node = queue.popleft()
            for next_node in graph[curr_node]:
                if min_times[next_node] == -1:  # Not visited before.
                    min_times[next_node] = min_times[curr_node] + 1
                    queue.append(next_node)

        earliest_idle_time = 0
        for i in range(1, n):
            # A data server can only send a new message BEFORE the first message comes back,
            # and since it takes the first message min_times[i] * 2 time to come back, the
            # available time to send a new message is min_times[i] * 2 - 1.
            one_trip_time = min_times[i] << 1
            extra_messages = (one_trip_time - 1) // patience[i]
            last_message_out_time = extra_messages * patience[i]
            last_message_in_time = last_message_out_time + one_trip_time

            earliest_idle_time = max(earliest_idle_time, last_message_in_time)

        return earliest_idle_time + 1  # Next second the network becomes idle.
