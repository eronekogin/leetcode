"""
https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/
"""


from heapq import heappush, heappop


class Solution:
    def busiestServers(
        self, k: int,
        arrival: list[int],
        load: list[int]
    ) -> list[int]:
        availableServers = list(range(k))
        busyServers = []
        requestCnt = [0] * k

        for i, startTime in enumerate(arrival):
            while busyServers and busyServers[0][0] <= startTime:
                """
                Based on the requirement, if we have 5 server and server 1, 4
                is currently free when handling the 12th request, the server 4
                should be considered first as 14 % 5 = 4, while server 1 should
                be considered secondly, which is 16 % 5 = 1. So in order to
                move those freed server to the right place in available heap,
                we can have:

                    while serverIndex < i:
                        serverIndex += k

                    avaialbleServers.push(serverIndex)

                since eventually serverIndex += k will be greater than k, this
                is the same as:

                    targerServerIndex = i + (serverIndex - i) % k
                """
                _, serverIndex = heappop(busyServers)
                heappush(availableServers, i + (serverIndex - i) % k)

            if availableServers:
                serverIndex = heappop(availableServers) % k
                heappush(busyServers, (startTime + load[i], serverIndex))
                requestCnt[serverIndex] += 1

        maxRequest = max(requestCnt)
        return [i for i, cnt in enumerate(requestCnt) if cnt == maxRequest]
