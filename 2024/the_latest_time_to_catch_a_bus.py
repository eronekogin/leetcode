"""
https://leetcode.com/problems/the-latest-time-to-catch-a-bus/description/
"""


class Solution:
    """
    Solution
    """

    def latest_time_catch_the_bus(
        self,
        buses: list[int],
        passengers: list[int],
        capacity: int
    ) -> int:
        """
        latest time catch the bus
        """
        sorted_buses = sorted(buses)
        sorted_passengers = sorted(passengers)

        b = p = 0
        m, n = len(buses), len(passengers)
        curr = 0

        while b < m:
            curr = 0

            while p < n and curr < capacity and sorted_passengers[p] <= sorted_buses[b]:
                p += 1
                curr += 1

            # Check at last bus.
            if b + 1 == m:
                p -= 1
                if curr < capacity:  # Last bus is not full.
                    t = sorted_buses[b]

                    while p >= 0 and t == sorted_passengers[p]:
                        p -= 1
                        t -= 1

                    return t

                # Otherwise the bus is full.
                t = sorted_passengers[p] - 1
                p -= 1
                while p >= 0 and t == sorted_passengers[p]:
                    p -= 1
                    t -= 1

                return t

            b += 1

        return sorted_buses[-1]


print(Solution().latest_time_catch_the_bus(
    [10, 20], [2, 17, 18, 19], 2))
