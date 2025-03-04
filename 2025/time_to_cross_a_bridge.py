"""
https://leetcode.com/problems/time-to-cross-a-bridge/description/
"""


from heapq import heappop, heappush


class Solution:
    """
    Solution
    """

    def find_crossing_time(self, n: int, k: int, time: list[list[int]]) -> int:
        """
        find crossing time
        """
        rslt = 0
        bridge_free_time = 0
        left_wait_workers: list[tuple[int, int]] = []
        left_cross_workers: list[tuple[int, int]] = []
        right_wait_workers: list[tuple[int, int]] = []
        right_cross_workers: list[tuple[int, int]] = []

        for i, (l, _, r, _) in enumerate(time):
            heappush(left_cross_workers, (-l - r, -i))

        while n or right_cross_workers or right_wait_workers:
            # Find the next free time
            if (
                not right_cross_workers and
                (
                    not right_wait_workers or
                    right_wait_workers[0][0] > bridge_free_time
                ) and
                (
                    not n or
                    not left_cross_workers and
                    (
                        not left_wait_workers or
                        left_wait_workers[0][0] > bridge_free_time
                    )
                )
            ):
                next_free = 10 ** 10
                if n and left_wait_workers:
                    next_free = min(next_free, left_wait_workers[0][0])

                if right_wait_workers:
                    next_free = min(next_free, right_wait_workers[0][0])

                bridge_free_time = next_free

            # Move worker to cross bridge queue before the next free time
            while right_wait_workers and right_wait_workers[0][0] <= bridge_free_time:
                _, i = heappop(right_wait_workers)
                heappush(right_cross_workers, (-time[i][0] - time[i][2], -i))

            while left_wait_workers and left_wait_workers[0][0] <= bridge_free_time:
                _, i = heappop(left_wait_workers)
                heappush(left_cross_workers, (-time[i][0] - time[i][2], -i))

            # Cross bridge
            if right_cross_workers:
                _, i = heappop(right_cross_workers)
                bridge_free_time += time[-i][2]
                if n:
                    heappush(
                        left_wait_workers,
                        (bridge_free_time + time[-i][3], -i)
                    )
                else:
                    rslt = max(rslt, bridge_free_time)
            else:
                _, i = heappop(left_cross_workers)
                bridge_free_time += time[-i][0]
                heappush(
                    right_wait_workers,
                    (bridge_free_time + time[-i][1], -i)
                )
                n -= 1

        return rslt
